from scipy.stats import hypergeom

a = hypergeom.pmf(1, 500, 10, 5)
print(a)