from praw_lib import *
import sys
import pyplot_lib as ppl
subreddits = ''
limit = 100
sql_dict = {'SQL': 0, 'Sequal': 0}
create_barchart = False
verbose = False
# if --help or -h appear in ANY of the command line args, print help and exit
if '--help' in sys.argv or '-h' in sys.argv:
    print('command line arguments for sql_or_squal:')
    print('-h or --help: display this message and exit successfully')
    print('-s or --subreddit [subreddit_list]: indicate in which subreddit(s) to search')
    print('-l or --limit: number of submissions to search per subreddit')
    print('--chart: no arguments, create a visual bar char of results')
    print('-v or --verbose: no arguments, log the name of the user and subreddit for each hit')
    sys.exit()

# command line args are (-s,--subreddit), (-l,--limit), (--chart)
for i,arg in enumerate(sys.argv): # go through all command line args
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
    if arg == '-v' or arg == '--verbose':
        verbose = True

if not subreddits: # exit with error code if no subreddit specified
    print('please provide at least one subreddit\nexample: "subreddit1+subreddit2"', file=sys.stderr)
    exit(1)
sql_dict = search_subreddits(subreddits = subreddits, limit = limit,verbose=verbose)
# print how often a sql or an sql was found
print(f"pronounce as 'SQL': {sql_dict['SQL']}")
print(f"pronounce as 'Sequal': {sql_dict['Sequal']}")

if create_barchart:
    ppl.create_sql_vs_sequal_chart(sql_dict)
