from scipy.stats import binom

alpha = 0.05
n = 100
N = 28
p_0 = 0.3

k = binom.ppf(alpha, n, p_0)
print(f"k: ", k)
r_k = binom.cdf(k, n, p_0)
r_k1 = binom.cdf(k-1, n, p_0)
print(f"r_k: ", r_k)
print(f"r_k1: ", r_k1)