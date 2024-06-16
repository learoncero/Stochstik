from scipy.stats import hypergeom, t, chi2, norm
import statistics
import math

# Aufgabe 4
N = 60
M = 10
n = 3

a1 = hypergeom.pmf(1, 60, 10, 3)
a2 = hypergeom.pmf(2, 60, 10, 3)
a3 = hypergeom.pmf(3, 60, 10, 3)

print(f"4) ", a1 + a2 + a3)

# Aufgabe 6
values = [124, 145, 112, 124, 136, 129, 125, 131, 142, 114]
n = len(values)

mean = statistics.mean(values)
s2 = statistics.variance(values)
s = math.sqrt(s2)

# Aufgabe 5
mu = 9
sigma = 0.707

z_value = (10 - mu) / sigma

# Berechnung der Wahrscheinlichkeit P(Z > z_value)
# P(Z > z_value) = 1 - P(Z <= z_value)
probability = 1 - norm.cdf(z_value)
print(f"5) probability: ", probability)

# Aufgabe 6
print(f"6) mean: ", mean) 
print(f"6) s2: ", s2) 
print(f"6) s: ", s) 

t_val = t.ppf(0.95, 9)
print(f"6) t_val: ", t_val) 

lower = mean - t_val * (s/math.sqrt(10))
upper = mean + t_val * (s/math.sqrt(10))
print(f"6) a) lower: ", lower) 
print(f"6) a) upper: ", upper) 

chi_val1 = chi2.ppf(0.95, 9)
chi_val2 = chi2.ppf(0.05, 9)
print(f"6) b) chi_val1: ", chi_val1) 
print(f"6) b) chi_val2: ", chi_val2) 

lower1 = (9 * s2)/chi_val1
upper1 = (9 * s2)/chi_val2
print(f"6) b) lower1: ", lower1) 
print(f"6) b) upper1: ", upper1) 

# Aufgabe 7
mu0 = 15
sigma = 0.04
n = 16
mean = 14.97
alpha = 0.05

z_val = ((mean - mu0)/(sigma/math.sqrt(n)))
print(f"7) z_val", z_val)
z_quan = norm.ppf(1-alpha)
print(f"7) z_quan", z_quan)
