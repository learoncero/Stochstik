from scipy.stats import norm
import numpy as np

mu = 800
sigma = 40

# a) n=16
n_a = 16
z_a = (790 - mu) / (sigma / np.sqrt(n_a))
p_a = norm.cdf(z_a)

# b) n=49
n_b = 49
z_b = (790 - mu) / (sigma / np.sqrt(n_b))
p_b = norm.cdf(z_b)

# c) n für 1.5% Wahrscheinlichkeit
z_c = norm.ppf(0.015)
n_c = ((sigma / (800 - 790)) * z_c) ** 2

print("a) n = 16: ", p_a)
print("b) n = 49: ", p_b)
print("c) n = ", n_c)