from scipy.stats import binom, t, norm, chi2
import numpy as np
import math

# Aufgabe 5
n = 2000
p = 0.0004

a = binom.pmf(2, n, p)
print("5) ", a)

# Aufgabe 7
n = 10
values = [124, 145, 112, 124, 136, 129, 125, 131, 142, 114]

mean = np.mean(values)
print("mean: ", mean)
variance = np.var(values, ddof=1)
print("variance: ", variance)
std_dev = math.sqrt(variance)
print("std_dev: ", std_dev)

t_val = t.ppf(0.95, 9)
print("t_val: ", t_val)
lower = (mean - t_val * (std_dev/math.sqrt(n)))
upper = (mean + t_val * (std_dev/math.sqrt(n)))

print("Intervall: [", lower, ", ", upper, "]")

chi2_val1 = chi2.ppf(0.95, 9)
chi2_val2 = chi2.ppf(0.05, 9)
print("chi2_val1: ", chi2_val1)
print("chi2_val2: ", chi2_val2)
lower_chi = ((n-1) * variance)/chi2_val1
upper_chi = ((n-1) * variance)/chi2_val2
print("Intervall: [", lower_chi, ", ", upper_chi, "]")
print("Intervall: [", math.sqrt(lower_chi), ", ", math.sqrt(upper_chi), "]")

# Aufgabe 8
mu0 = 420
n = 16
alpha = 0.05
mean = 408
s = 25.7

t_val = (mean - mu0)/(s/math.sqrt(n))
print("t_val: ", t_val)
t_quan = t.ppf(1-alpha, n-1)
print("t_quan: ", t_quan)