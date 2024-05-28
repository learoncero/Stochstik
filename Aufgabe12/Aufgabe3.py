from scipy.stats import chi2

n = 40
alpha = 0.05
s2 = 0.0107
variance = 0.01

y = (n-1) * s2 / variance
critical_value = chi2.ppf(1 - alpha, n-1)

print(f"y: {y}")
print(f"critical_value: {critical_value}")