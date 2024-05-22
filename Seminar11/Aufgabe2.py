import numpy as np
from scipy.stats import t, chi2

data = [20.7, 17.3, 26.4, 40.9, 20.4, 25.7, 27.3, 18.0]
n = len(data)
mean = np.mean(data)
s = np.std(data, ddof=1)


# a)
standard_error = s / np.sqrt(n)
t_value = t.ppf(1 - 0.05, n-1)
margin_of_error = t_value * standard_error
lower_bound = mean - margin_of_error
upper_bound = mean + margin_of_error

print(f"a) Das Konfidenzintervall lautet: [{lower_bound}, {upper_bound}]")

# b)
alpha = 0.05
chi2_upper = chi2.ppf(alpha / 2, n - 1)
chi2_lower = chi2.ppf(1 - alpha / 2, n - 1)
variance = s ** 2
lower_bound_var = (n - 1) * variance / chi2_lower
upper_bound_var = (n - 1) * variance / chi2_upper

print(f"b) Das Konfidenzintervall für die Varianz lautet: [{lower_bound_var}, {upper_bound_var}]")