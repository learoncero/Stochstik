from scipy.stats import t, chi2
import math

# Aufgabe 3
# a)

n = 10
x_mean = 748.2
s_2 = 15.6
s = math.sqrt(s_2)

t_val = t.ppf(0.995, df=n-1)
print(t_val)
print(s)

lower = 748.2 - t_val * (s/math.sqrt(n))
upper = 748.2 + t_val * (s/math.sqrt(n))

print(lower)
print(upper)


# b)
alpha = 0.05
b = ((n-1) * s_2) / (chi2.ppf(1-alpha, n-1))

print(b)