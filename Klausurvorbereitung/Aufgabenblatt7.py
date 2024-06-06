from scipy.stats import hypergeom
from scipy.stats import poisson

# Aufgabe 7.2

N = 52
M = 11
n = 20

# a)
k = 2
a = hypergeom.pmf(k, 52, 11, 20)
print(a)

# b)
k = 0
b = hypergeom.pmf(k, 52, 11, 20)
print(b)

# c)
k = 20
c = hypergeom.pmf(k, 52, 11, 20)
print(c)

# d)
k = 11
d = hypergeom.pmf(k, 52, 11, 20)
print(d)

# e)
e = 1 - hypergeom.pmf(0, 52, 11, 20)
print(e)

# Aufgabe 7.3

# a)
lam = 3
a = 1 - poisson.cdf(3, lam)
print(a)

# b)
lam = 15
b = 1 - poisson.cdf(19, lam)
print(b)