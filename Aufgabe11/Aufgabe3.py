from scipy.stats import norm
from scipy.stats import chi2
from scipy.stats import t

n = 10
mean = 748.2
variance = 15.6
alpha = 0.01

# a)
z = norm.ppf(1-alpha/2)
print(f"z: {z}")
t_value = t.ppf(1-alpha/2, df=n-1)
print(f"t_value: {t_value}")
sigma = variance**0.5
confidence_interval = (mean - z*sigma/n**0.5, mean + z*sigma/n**0.5)

print(f"confidence interval: {confidence_interval}")

# b)
alpha_b = 0.05
chi2_critical_b = chi2.ppf(1-alpha_b, df=n-1)
print(f"chi2_critical_b: {chi2_critical_b}")

# Untere Konfidenzschranke
untere_schranke = (n-1) * variance / chi2_critical_b
print(f"untere_schranke: {untere_schranke}")
