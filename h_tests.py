# allow user to input their own hypothesis
# but still default to 50% pronouncing sql and
# 50% pronouncing sequal
def perform_chisquare(o,e):
    from scipy import stats
    res = stats.chisquare(o,e)
    print(f'pvalue: {res.pvalue}') 
    print(f'test statistic: {res.statistic}')
if __name__ == '__main__':
    perform_chisquare([12,10], [11,11])
