from scipy.stats import norm

mu = 2000
sigma = 20

# a)
p_greater_2500 = 1 - norm.cdf(2500, mu, sigma)
print(p_greater_2500)

#b)
p_between_1900_and_1600 = norm.cdf(1900, mu, sigma) - norm.cdf(1600, mu, sigma)
print(p_between_1900_and_1600)