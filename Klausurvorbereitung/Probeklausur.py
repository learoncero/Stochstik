from scipy.stats import poisson, expon, t
import numpy as np
import math
import statistics

a1 = poisson.pmf(2, 1)
a2 = poisson.pmf(3, 1)
a3 = poisson.pmf(4, 1)
print(f"a1", a1)
print(f"a2", a2)
print(f"a3",a3)
print(f"a1 + a2 + a3", a1 + a2 + a3)

c = expon.cdf(0.75 * 3)
print(f"c", c)
d = expon.ppf(0.95, scale=1/3)
print(f"d*60", d*60)

data = [2.81, 2.62, 2.96, 3.03, 3.23, 3.31, 2.82, 3.21, 2.84, 3.20]
e = np.mean(data)
f = statistics.variance(data)
print(f"e", e)
print(f"f", f)

t_val = t.ppf(0.975, 99)
print(t_val)
lower = (3 - (t_val * (math.sqrt(0.09)/10)))
upper = (3 + (t_val * (math.sqrt(0.09)/10)))
print(f"lower", lower)
print(f"upper", upper)

values = [101, 98, 96, 102,99, 101, 102, 103, 96, 97]
mean = np.mean(values)
var = np.var(values)
std_dev = math.sqrt(var)

print(f"mean", mean)
print(f"var", var)
print(f"std_dev", std_dev)

t_val = ((mean-100)/(std_dev/math.sqrt(10)))
print(f"t_val", t_val)
crit_val = t.ppf(0.95, 9)
print(f"crit_val", crit_val)