from scipy.stats import norm

n = 10
mean = 748.2
variance = 15.6
alpha = 0.01

# a)
z = norm.ppf(1-alpha/2)
print(f"z: {z}")
sigma = variance**0.5
confidence_interval = (mean - z*sigma/n**0.5, mean + z*sigma/n**0.5)

print(f"confidence interval: {confidence_interval}")