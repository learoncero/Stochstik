from scipy.stats import chi2, norm, t
import numpy as np
import math

# a)
values = [7.2, 8.2, 7.0, 9.2, 8.1, 6.9, 7.1, 8.5, 9.0, 8.5]
n = len(values)
alpha = 0.05

x_mean = np.mean(values)
variance = np.var(values, ddof=1)

print(f"x_mean", {x_mean})
print(f"variance", variance)

chi_val1 = chi2.ppf(1-(alpha/2), n - 1)
chi_val2 = chi2.ppf((alpha/2), n - 1)

print(f"chi_value1", chi_val1)
print(f"chi_value2", chi_val2)

lower = ((n-1) * variance) / chi_val1
upper = ((n-1) * variance) / chi_val2
print(f"lower", lower)
print(f"upper", upper)

# b)
variance = 0.5
alpha = 0.05

z_val = norm.ppf(1-(alpha/2))
print(f"z_val", z_val)

lower = x_mean - z_val * (math.sqrt(variance)/math.sqrt(n)) 
upper = x_mean + z_val * (math.sqrt(variance)/math.sqrt(n)) 

print(f"lower", lower)
print(f"upper", upper)

# c)
alpha = 0.05
variance = np.var(values, ddof=1)
t_val = t.ppf(1-(alpha/2), n-1)
print(f"t_val", t_val)

lower = x_mean - t_val * (math.sqrt(variance)/math.sqrt(n)) 
upper = x_mean + t_val * (math.sqrt(variance)/math.sqrt(n)) 

print(f"lower", lower)
print(f"upper", upper)