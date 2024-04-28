from scipy.stats import expon
from math import exp

result = expon.cdf(3000, scale=3000)
print(result)

result1 = 1 - exp(-1)
print(result1)