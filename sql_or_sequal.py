from praw_lib import *
import argparse
import sys
import pyplot_lib as ppl
from scipy import stats 
parser = argparse.ArgumentParser() # add description
parser.add_argument('--subreddits', '-s', type=str, required=True)
parser.add_argument('--limit','-l', type=int,default=100)
parser.add_argument('--chart', action='store_true')
parser.add_argument('--verbose','-v',action='store_true')
parser.add_argument('--chisquare',type=float, default=None, const=1, nargs='?')
args = parser.parse_args()
sql_dict = {'SQL': 0, 'Sequal': 0}
# if --help or -h appear in ANY of the command line args, print help and exit
if '--help' in sys.argv or '-h' in sys.argv:
    print('command line arguments for sql_or_squal:')
    print('-h or --help: display this message and exit successfully')
    print('-s or --subreddit [subreddit_list]: indicate in which subreddit(s) to search')
    print('-l or --limit: number of submissions to search per subreddit.  default is 100')
    print('--chart: no arguments, create a visual bar char of results')
    print('-v or --verbose: no arguments, log the name of the user and subreddit for each hit')
    print('--chisquare: perform chisquare goodness of fit test, optional argument is ratio of sql to sequal.  Default arg is 1')
    sys.exit()

sql_dict = search_subreddits(subreddits = args.subreddits, limit = args.limit,verbose=args.verbose)
# print how often a sql or an sql was found
print(f"pronounce as 'SQL': {sql_dict['SQL']}")
print(f"pronounce as 'Sequal': {sql_dict['Sequal']}")

if args.chart:
    ppl.create_sql_vs_sequal_chart(sql_dict)

if args.chisquare is not None:
    o = [sql_dict['SQL'], sql_dict['Sequal']]
    total = sql_dict['SQL'] + sql_dict['Sequal']
    expected_sql = (args.chisquare / (args.chisquare + 1)) * total
    expected_sequal = total - expected_sql
    e = [expected_sql, expected_sequal]
    res = stats.chisquare(o,e)
    print(f'chi-square GOF pvalue: {res.pvalue}') 
    print(f'chi-square GOF test statistic: {res.statistic}')
