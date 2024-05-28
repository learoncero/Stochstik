import numpy as np
from scipy.stats import t

mean = 408
s = 25.7
n = 16
mu_0 = 420

t_value = (mean - mu_0) / (s / np.sqrt(n))

alpha_05 = 0.05
alpha_01 = 0.01

t_critical_05 = t.ppf(alpha_05, n - 1)
t_critical_01 = t.ppf(alpha_01, n - 1)

print(f"t_value: {t_value}")    
print(f"t_critical_05: {t_critical_05}")
print(f"t_critical_01: {t_critical_01}")