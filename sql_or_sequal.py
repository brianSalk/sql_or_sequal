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
sql_dict = defaultdict(int)
# count occurances of 'an sql' and 'a sql' from each user
user_dict = defaultdict(lambda : [0,0])
# count occurances of 'an sql' and 'a sql' within each subreddit

def log_match(mtch, sub, user):
    logging.info( "'" + mtch + "'" + " found in subreddit " + sub + " by user " + user)

def sql_regex(text, submission=None, comment = None):
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
        sql_dict[each_match] += 1
        if re.match(a_sql,each_match):
            user_dict[user][0]+=1
        else:
            user_dict[user][1]+=1

        

def search_subreddits(subreddits,limit = 1000):
    for submission in reddit.subreddit(subreddits).new(limit=limit):
        #print(submission.title)
        comment_forest = submission.comments.replace_more(limit=100)
        sql_regex(submission.title, submission=submission)
        sql_regex(submission.selftext, submission)
        for comment in comment_forest:
            sql_regex(comment.selftext, comment=comment)

#sql_regex("this is a sQl program TEST TEXT")
#sql_regex("this is an sQl program TEST TEXT")
#sql_regex("this is nota sql program")
#sql_regex("an sql program")
#sql_regex("a good sql table")
search_subreddits(subreddits="mysql", limit = 1000)
print(sql_dict)
print(user_dict)

# pickle stuff

#sql_dict_file = open("pickle_objects/sql_dict", "wb")
#user_list = []
#for key,val in user_dict.items():
#    user_list.append([key,val])
#user_list_file = open("pickle_objects/user_list", "wb")
#pickle.dump(user_list,user_list_file)
#pickle.dump(sql_dict, sql_dict_file)
#sql_dict_file.close()
#user_list_file.close()
