from scipy.stats import binom

alpha = 0.05
n = 200
p_0 = 0.1

k = binom.ppf(1-alpha, n, p_0)
print(k)
res1 = binom.cdf(k, n, p_0)
res2 = binom.cdf(k+1, n, p_0)
res3 = binom.cdf(k+2, n, p_0)
print(res1)
print(1-res1)
print(res2)
print(1-res2)
print(res3)
print(1-res3)
print(alpha/2)