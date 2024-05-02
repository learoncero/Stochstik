from scipy.stats import norm
import numpy as np

mu = 72
sigma = 9
X = 75

# a) n=40, mu=75, sigma=9
n_a = 40
z_a = (X - mu) / (sigma / np.sqrt(n_a))
p_a = 1 - norm.cdf(z_a)
print("a) n = 40, X=75: ", p_a)

# b) n=1
n_b = 1
z_b = (X - mu) / (sigma / np.sqrt(n_b))
p_b = 1 - norm.cdf(z_b)
print("b) n = 1, X=75: ", p_b)