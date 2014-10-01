from scipy import stats
k = 6
N = 17
n = 2**k
print 1 - stats.binom.cdf(N-1, n, 1/4.0)

