import praw
import re
import pickle
import sys, logging
import credentials as c
from collections import defaultdict
logging.basicConfig(format='%(levelname)s:%(message)s',level=logging.INFO)

reddit = praw.Reddit(
        client_id = c.client_id,
        client_secret = c.client_secret,
        user_agent = c.user_agent,
        username = c.username,
        password = c.password
        )
#print(reddit.user.me())
# count each occurance of 'an sql' or 'a sql'
#sql_dict = defaultdict(int)
# count occurances of 'an sql' and 'a sql' from each user
#user_dict = defaultdict(lambda : [0,0])
# count occurances of 'an sql' and 'a sql' within each subreddit
# NOT HERE YET
def log_match(mtch, sub, user):
    logging.info( "'" + mtch + "'" + " found in subreddit " + sub + " by user " + user)

def sql_regex(text, submission=None, comment = None, sql_dict=None):
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
        log_match(each_match, sub, user)
        each_match = each_match.lower()
        each_match = " ".join(each_match.split())
        if each_match == 'a sql':
            sql_dict['Sequal'] += 1
        elif each_match == 'an sql':
            sql_dict['SQL'] += 1

        
def get_invalid_subreddits(subreddits_list):
    invalid_list = []
    for sub in subreddits_list:
        for each in subreddits_list:
            try:
                reddit.subreddits.search_by_name(each, exact=True)
            except Exception as e:
                #print(e)
                invalid_list.append(each)
        return invalid_list
def search_subreddits(subreddits,limit = 1000,user_dict=None,sql_dict=None):
    subreddits = subreddits.split('+')
    invalid = get_invalid_subreddits(subreddits)
    if len(invalid) > 0:
        print('the following subreddit(s) do not exist')
        print(invalid)
        sys.exit(1)
        
    for each_sub in subreddits:
        sdict = defaultdict(int)
        for submission in reddit.subreddit(each_sub).new(limit=limit):
            #print(submission.title)
            comment_forest = submission.comments.replace_more(limit=100)
            sql_regex(submission.title, submission=submission, sql_dict=sdict)
            sql_regex(submission.selftext, submission, sql_dict=sdict)
            for comment in comment_forest:
                sql_regex(comment.selftext, comment=comment, sql_dict=sdict)
        for key,val in sdict.items():
            sql_dict[key] += val


