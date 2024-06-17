from scipy.stats import norm, hypergeom, poisson, binom, expon
import math
import statistics

n = 5
N = 30
M = 10
k = 2

# Hypergeometrische Verteilung
hyper = hypergeom.pmf(k,N,M,n)
print("hyper: ", hyper)

# Binomialverteilung
n = M/N
p = M/N
binom = binom.pmf(k, n, p)
print("binom: ", binom)

# Poisson-Verteilung
mu = n * (M/N)
poisson = poisson.pmf(k, mu)
print("poisson: ", poisson)

# Normalverteilung
sigma = math.sqrt(n * ((M*(N-M)*(N-n)) / (N*N*(N-1))))
norm = norm.ppf(k, mu, sigma)
print("norm: ", norm)


# Exponentialverteilung
mu = 1000
lamda = 1/mu
x = 500
result = expon.cdf(x*lamda)
print(f"result expon: ", result)
