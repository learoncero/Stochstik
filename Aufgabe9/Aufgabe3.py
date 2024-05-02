from scipy.stats import norm

sigma = 6
X = 0.5

z_value = norm.ppf(0.995)
print(z_value)

n = (z_value * sigma / X) ** 2

print("n=", n)