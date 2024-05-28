import numpy as np
from scipy.stats import t

mean = 70
s = 15
n = 20
mu_0 = 60

t_value = (mean - mu_0) / (s / np.sqrt(n))

alpha_05 = 0.05

t_critical_05 = t.ppf(alpha_05, n - 1)

print(f"t_value: {t_value}")    
print(f"t_critical_05: {t_critical_05}")