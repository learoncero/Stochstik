from scipy.stats import norm

result = norm.cdf(25, 15, 5) - norm.cdf(20, 15, 5)
print(result)