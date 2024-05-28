from scipy.stats import norm

mu_0 = 7.6
n = 40
sigma = 0.6
mean = 7.8
alpha = 0.05

z = (mean - mu_0) / (sigma / n**0.5)
critical_value = norm.ppf(1 - alpha)

print(f"z: {z}")
print(f"critical_value: {critical_value}")