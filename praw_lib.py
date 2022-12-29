import praw
import re
import pickle
import sys, logging
import credentials as c
import multiprocessing as mp
from collections import defaultdict
# set log level
logging.basicConfig(format='%(levelname)s:%(message)s',level=logging.INFO)
# authorize app first time
reddit = praw.Reddit(
        client_id = c.client_id,
        client_secret = c.client_secret,
        user_agent = c.user_agent,
        username = c.username,
        password = c.password
        )
def log_match(mtch, sub, user):
    """
    log info about the match that was found
    """
    logging.info( "'" + mtch + "'" + " found in subreddit " + sub + " by user " + user)

def sql_regex(text, submission=None, comment = None, sql_dict=None, verbose=False):
    """
    if regex match found, incrament dict at corresponding key 
    """
    user = ""
    sub = ""
    if submission:
        if submission.author:
            user = submission.author.name
        else:
            user = "DELETED" # if user deleted their name, this line will prevent a runtime error.  
        sub = submission.subreddit.display_name
    elif comment:
        if comment.author:

            user = comment.author.name
        else:
            user = "DELETED"
        sub = comment.subreddit.display_name

    mtch = re.findall(r'\ban?\s+sql\b',text,re.I)
    a_sql = re.compile(r'^a sql$')
    an_sql = re.compile(r'^an sql$')
    for each_match in mtch:
        if verbose:
            log_match(each_match, sub, user)
        each_match = each_match.lower()
        each_match = " ".join(each_match.split())
        if each_match == 'a sql':
            sql_dict['Sequal'] += 1
        elif each_match == 'an sql':
            sql_dict['SQL'] += 1

        
def get_invalid_subreddits(subreddits_list):
    """
    if one or more subreddit is invalid, return in list,
    if no invalid subreddits, return empty list
    """
    invalid_list = []
    for sub in subreddits_list:
        for each in subreddits_list:
            try:
                reddit.subreddits.search_by_name(each, exact=True)
            except Exception as e:
                invalid_list.append(each)
        return invalid_list
def search_subreddit(each_sub, mp_list,limit,verbose=False):
    """
    search submissions and comments in subreddit
    """
    # initialize Reddit object again to avoid SSL error
    reddit = praw.Reddit(
            client_id = c.client_id,
            client_secret = c.client_secret,
            user_agent = c.user_agent,
            username = c.username,
            password = c.password
            )
    sdict = defaultdict(int)
    for submission in reddit.subreddit(each_sub).new(limit=limit):
        comment_forest = submission.comments.replace_more(limit=100)
        sql_regex(submission.title, submission=submission, sql_dict=sdict,verbose=verbose)
        sql_regex(submission.selftext, submission, sql_dict=sdict, verbose=verbose)
        for comment in comment_forest:
            sql_regex(comment.selftext, comment=comment, sql_dict=sdict, verbose=verbose)
    mp_list.append(sdict)



def search_subreddits(subreddits,limit = 1000,verbose=False):
    """
    loop over all subreddits, start new process for each
    subreddit
    """
    subreddits = subreddits.split('+')
    invalid = get_invalid_subreddits(subreddits)
    if len(invalid) > 0:
        print('the following subreddit(s) do not exist')
        print(invalid)
        sys.exit(1)
    with mp.Manager() as manager:
        # mp_list is a list of dicts.  I needed to use manager.list()
        # because I cannot safely append to a python dict asyncronously.
        mp_list = manager.list()
        processes = []
        for each_sub in subreddits:
            # start new process each time this is called
            p = mp.Process(target=search_subreddit, args=(each_sub,mp_list,limit,verbose))
            p.start()
            processes.append(p)
        for proc in processes:
            proc.join()
        # create ans, the dict containing the final SQL and Sequal counts.
        ans = defaultdict(int)
        for each in mp_list:
            for key,val in each.items():
                ans[key] += val
        return ans
