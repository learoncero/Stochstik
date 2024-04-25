from scipy.stats import poisson

n = 32 + 28 + 14 + 5 + 1 + 0
print(n)

lamda = (0 * 0.4) + (1 * 0.35) + (2 * 0.175) + (3 * 0.0625) + (4 * 0.0125) + (5 * 0)
print(lamda)

r1 = poisson.pmf(0, 0.9375)
r2 = poisson.pmf(1, 0.9375)
r3 = poisson.pmf(2, 0.9375)
r4 = poisson.pmf(3, 0.9375)
r5 = poisson.pmf(4, 0.9375)
r6 = poisson.pmf(5, 0.9375)

print(r1)
print(r2)
print(r3)
print(r4)
print(r5)
print(r6)
