from scipy.stats import norm

# Aufgabe 6

# a)
mu = 2000
variance = 400

a = 1 - norm.cdf(2500, mu, variance)
print(a)

# b) 
z1 = (1600 - 2000) / 400
z2 = (1900 - 2000) / 400
b = norm.cdf(z2) - norm.cdf(z1)
print(b)

# c)
upper_quartile = norm.ppf(0.75, 2000, 400)
print(upper_quartile)

# d)
z = norm.ppf(0.975)
a = z * 400

d1 = 2000 - a
d2 = 2000 + a

print (d1, d2)