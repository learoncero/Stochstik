from scipy.stats import norm
import math

# Aufgabe 1
mu = 800
sigma = 40

# a)
n1 = 16
a = norm.cdf(-1)
print(a)

# b)
z = (790-800) / (40/math.sqrt(49))
b = norm.cdf(z)

print(b)

# Aufgabe 2
mu = 72
sigma = 9

#  a)
z = ((75 - mu) / (9 / math.sqrt(40)))
a = 1 - norm.cdf(z)
print(a)

# b)
z = (3 / 9)
b = 1 - norm.cdf(z)
print(b)