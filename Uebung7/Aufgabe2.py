from scipy.stats import hypergeom

M = 11
N = 52
n = 20

# a)
X = 2

pmf_a = hypergeom.pmf(X, N, M, n)
print("a) Die Wahrscheinlichkeit von ", X, " Erfolgen beträgt ", pmf_a)

# b)
X = 0

pmf_b = hypergeom.pmf(X, N, M, n)
print("b) Die Wahrscheinlichkeit von ", X, " Erfolgen beträgt ", pmf_b)

# c)
X = 20

pmf_c = hypergeom.pmf(X, N, M, n)
print("c) Die Wahrscheinlichkeit von ", X, " Erfolgen beträgt ", pmf_c)

# d)
X = 11

pmf_d = hypergeom.pmf(X, N, M, n)
print("d) Die Wahrscheinlichkeit von ", X, " Erfolgen beträgt ", pmf_d)

# e)
X = 0
pmf_e = 1 - hypergeom.pmf(X, N, M, n)
print("d) Die Wahrscheinlichkeit von mindestens einem Erfolg beträgt ", pmf_e)
