from scipy.stats import chi2

alpha = 0.05
variance = 100

# a)
n = 10

chi2_upper = chi2.ppf(alpha / 2, n - 1)
chi2_lower = chi2.ppf(1 - alpha / 2, n - 1)
lower_bound_var = (n - 1) * variance / chi2_lower
upper_bound_var = (n - 1) * variance / chi2_upper

print(f"a) Das Konfidenzintervall für die Varianz lautet: [{lower_bound_var}, {upper_bound_var}]")

# b)
n = 100

chi2_upper = chi2.ppf(alpha / 2, n - 1)
chi2_lower = chi2.ppf(1 - alpha / 2, n - 1)
lower_bound_var = (n - 1) * variance / chi2_lower
upper_bound_var = (n - 1) * variance / chi2_upper

print(f"b) Das Konfidenzintervall für die Varianz lautet: [{lower_bound_var}, {upper_bound_var}]")