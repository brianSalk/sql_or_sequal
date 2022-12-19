from praw_lib import *
import argparse
import sys
import pyplot_lib as ppl
from scipy import stats 
# ----setup argparse stuff ----------------------------------------
parser = argparse.ArgumentParser() # add description
parser.add_argument('--subreddits', '-s', type=str, required=True, help='list of subreddit to search, seperate with + e.g mysql+sql+database', metavar='SUBREDDIT_LIST')
parser.add_argument('--limit','-l', type=int,default=100,metavar='N', help='limit number of submissions to search in subreddit to N, default 100')
parser.add_argument('--chart', action='store_true', help='create a barchar of the results')
parser.add_argument('--verbose','-v',action='store_true', help='log username and subreddit of each match to stderr')
parser.add_argument('--chisquare',type=float, default=None, const=1, nargs='?', help='perform chisquared goodness of fit test.  optional argument is ratio of SQL to Sequal, for example if you expect that the ratio of SQL to Sequal is 2:1, you would give --chisquare 2, if you expect 1 SQL for every 3 Sequals, --chisqare .3333333333')
args = parser.parse_args()
if args.limit <= 0:
    print(f'argument to limit must be a non-negative integer',file=sys.stderr)
    sys.exit(1)
# -------- end setup parsearg stuff ------------------------------
sql_dict = {'SQL': 0, 'Sequal': 0}

sql_dict = search_subreddits(subreddits = args.subreddits, limit = args.limit,verbose=args.verbose)
# print how often a sql or an sql was found
print(f"pronounce as 'SQL': {sql_dict['SQL']}")
print(f"pronounce as 'Sequal': {sql_dict['Sequal']}")

# print barchart if --chart arg present
if args.chart:
    ppl.create_sql_vs_sequal_chart(sql_dict)

# print chisquare GOF test if --chisquare arg present
if args.chisquare is not None:
    o = [sql_dict['SQL'], sql_dict['Sequal']]
    total = sql_dict['SQL'] + sql_dict['Sequal']
    expected_sql = (args.chisquare / (args.chisquare + 1)) * total
    expected_sequal = total - expected_sql
    e = [expected_sql, expected_sequal]
    res = stats.chisquare(o,e)
    print(f'chi-square GOF pvalue: {res.pvalue}') 
    print(f'chi-square GOF test statistic: {res.statistic}')

