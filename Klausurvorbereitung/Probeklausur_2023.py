from scipy.stats import binom

# Aufgabe 5
n = 2000
p = 0.0004

a = binom.pmf(2, n, p)
print("5) ", a)