from scipy.stats import binom

# a)
result1 = binom.cdf(3, 20, 0.05)
print(result1)

# b)
result2 = binom.isf(0.1, 20, 0.05)
print(result2)