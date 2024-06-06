from scipy.stats import norm
import math

# Aufgabe 5
mu = 320
sigma = (80**0.5) * 0.1
x = 310

a1 = norm.cdf(310,320, 0.8944)
a2 = norm.cdf((x-mu)/sigma)
print(a1)
print(a2)

# Aufgabe 7
b = norm.cdf(14400, 18750, 18750)
print(b)

# Aufgabe 8
mu = 564
sigma_squared = 2910
n = 50
sigma = math.sqrt(sigma_squared)

sigma_G = sigma / math.sqrt(n)
G_bar = 560
z = (G_bar - mu) / sigma_G

c = 1 - norm.cdf(z)
print(c)