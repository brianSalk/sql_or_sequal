# allow user to input their own hypothesis
# but still default to 50% pronouncing sql and
# 50% pronouncing sequal
from scipy import stats
def perform_chisquare(o,e):
    res = stats.chisquare(o,e)
    print(f'chi-square GOF pvalue: {res.pvalue}') 
    print(f'chi-square GOF test statistic: {res.statistic}')
