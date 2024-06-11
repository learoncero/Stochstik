from scipy.stats import poisson, expon, t
import numpy as np
import math

a = poisson.cdf(4, 1)
b = poisson.cdf(1, 1)

print(a)
print(b)
print(a - b)

c = expon.cdf(0.75 * 3)
print(c)
d = expon.ppf(0.95, scale=1/3)
print(d*60)

data = [2.81, 2.62, 2.96, 3.03, 3.23, 3.31, 2.82, 3.21, 2.84, 3.20]
e = np.mean(data)
f = np.var(data)
print(e)
print(f)

t_val = t.ppf(0.975, 99)
print(t_val)
lower = (3 - (t_val * (math.sqrt(0.09)/10)))
upper = (3 + (t_val * (math.sqrt(0.09)/10)))
print(lower)
print(upper)

values = [101, 98, 96, 102,99, 101, 102, 103, 96, 97]
mean = np.mean(values)
var = np.var(values)
std_dev = math.sqrt(var)

print(mean)
print(var)
print(std_dev)

t_val = ((mean-100)/(std_dev/math.sqrt(10)))
print(t_val)
crit_val = t.ppf(0.95, 9)
print(crit_val)