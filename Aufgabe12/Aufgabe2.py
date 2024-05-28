from scipy.stats import t

mu_0 = 72.6
n = 120
mean = 75.8
s = 7.5
alpha = 0.01

t_value = (mean - mu_0) / (s / n**0.5)
t_critical = t.ppf(1 - alpha, n - 1)

print(f"t_value: {t_value}")
print(f"t_critical: {t_critical}")