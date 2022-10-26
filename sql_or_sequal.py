from lib import *
import sys
subreddits = ''
limit = 100
for i,arg in enumerate(sys.argv):
    if i == 0:
        continue
    if arg == '--subreddit' or arg == '-s':
        if i == len(sys.argv)-1:
            print(f"mandatory argument to '{arg}' not provided\nplease provide a list of at least one subreddit seperated by '+'",file=sys.stderr)
            exit(1)
        else:
            subreddits = sys.argv[i+1]
    if arg == '--limit' or arg == '-l':
        if i == len(sys.argv)-1:
            print(f"mandatory argument to '{arg}' not provided\nplease provide a positive integer (100 is default)",file=sys.stderr)
            exit(1)
        else:
            limit = int(sys.argv[i+1])

if not subreddits:
    print('please provide at least one subreddit', file=sys.stderr)
    exit(1)
search_subreddits(subreddits = subreddits, limit = limit)
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
