from scipy.stats import chi2

n = 76
s2 = 14
variance = 16

y = (n-1) * s2 / variance

alpha = 0.05
critical_value_left = chi2.ppf(alpha/2, n-1)
critical_value_right = chi2.ppf(1 - alpha/2, n-1)

print(f"y: {y}")
print(f"critical_value_left: {critical_value_left}")
print(f"critical_value_right: {critical_value_right}")