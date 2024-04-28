from math import exp
from scipy.stats import expon

result = 1 - exp(-267/2000)
print(result)

result1 = expon.cdf(267, scale=2000)
print(result1)