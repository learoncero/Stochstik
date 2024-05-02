from scipy.stats import norm

# a) 

# Known values from the percentiles
p_less_1 = 0.01  # 1st percentile
p_greater_20 = 0.20  # Upper tail for 20

# Inverse CDF to find Z-values
z_1 = norm.ppf(p_less_1)
z_20 = norm.ppf(1 - p_greater_20)

# Equations based on Z-scores
# z_1 = (1 - mu) / sigma
# z_20 = (20 - mu) / sigma

# Solve the equations for mu and sigma
mu = (z_20 - z_1) / (20 - 1)
sigma = (20 - mu) / z_20

print(mu, sigma)

# b) P(X = 20)
p_20 = norm.pdf(20, mu, sigma)
print(p_20)

# c) P(X <= 20)
p_less_20 = norm.cdf(20, mu, sigma)
print(p_less_20)


# d) P(X >= 25)
p_greater_25 = 1 - norm.cdf(25, mu, sigma)
print(p_greater_25)

# e) P(X >= 25|X >= 20)
p_greater_20 = 1 - norm.cdf(20, mu, sigma)
p_25_given_20 = p_greater_25/p_greater_20
print(p_25_given_20)

# f) P(X >= 20|X >= 25)
p_20_given_25 = p_greater_25 / p_greater_25
print(p_20_given_25)