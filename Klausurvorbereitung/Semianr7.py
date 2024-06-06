from scipy.stats import binom
from scipy.stats import hypergeom

# 2) 
p = 0.03
n = 50

# a)
k = 0
a = binom.pmf(k, n, p)
print(a)

# b)
k = 2
b = binom.pmf(k, n, p)
print(b)

# c)
k = 1
c = binom.pmf(k, n, p)
print(c)
print(a + b + c)

c1 = binom.cdf(2, n, p)
print(c1)

# 3) 
p = 0.05
n = 20

# a)
k = 3
a = binom.cdf(k, n, p)
print(a)

# b)
y = 0.1
k = binom.isf(y,n,p)
print(k)

# 4)
N = 500
M = 10
n = 5
k = 1

res = hypergeom.pmf(k,N,M,n)
print(res)