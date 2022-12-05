from praw_lib import *
import sys
import pyplot_lib as ppl
subreddits = ''
limit = 100
create_barchart = False
for i,arg in enumerate(sys.argv):
    if i == 0:
        continue
    if arg == '--subreddit' or arg == '-s':
        if i == len(sys.argv)-1:
            print(f"mandatory argument to '{arg}' not provided\nplease provide a list of at least one subreddit seperated by '+'\nexample: 'subreddit1+subreddit2'",file=sys.stderr)
            exit(1)
        else:
            subreddits = sys.argv[i+1]
    if arg == '--limit' or arg == '-l':
        if i == len(sys.argv)-1:
            print(f"mandatory argument to '{arg}' not provided\nplease provide a positive integer (100 is default)",file=sys.stderr)
            exit(1)
        else:
            limit = int(sys.argv[i+1])
    if arg == '--chart':
        create_barchart = True

if not subreddits:
    print('please provide at least one subreddit\nexample: "subreddit1+subreddit2"', file=sys.stderr)
    exit(1)
search_subreddits(subreddits = subreddits, limit = limit)
print(f"pronounce as 'SQL': {sql_dict['SQL']}")
print(f"pronounce as 'Sequal': {sql_dict['Sequal']}")
#print(user_dict)
if create_barchart:
    ppl.create_sql_vs_sequal_chart(sql_dict)

