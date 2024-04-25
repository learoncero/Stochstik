from scipy.stats import poisson

# Poisson distribution

# a)
lambda_val = 3
x = 3

result = 1 - poisson.cdf(x, lambda_val)
print("a) ", result)


# b)
lambda_val = 15
x = 19

result = 1 - poisson.cdf(x, lambda_val)
print("b) ", result)