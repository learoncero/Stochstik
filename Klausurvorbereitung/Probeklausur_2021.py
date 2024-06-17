import scipy.stats as stats

# Mittelwert und Standardabweichung
mu = 960
sigma = 6.2

# Teil (a): Wahrscheinlichkeit, dass höchstens 940 Samen keimen
z_a = (940 - mu) / sigma
p_a = stats.norm.cdf(z_a)

# Teil (b): Wahrscheinlichkeit, dass mindestens 940 und höchstens 970 Samen keimen
z_b1 = (940 - mu) / sigma
z_b2 = (970 - mu) / sigma
p_b = stats.norm.cdf(z_b2) - stats.norm.cdf(z_b1)

# Teil (c): Wahrscheinlichkeit, dass mindestens 960 Samen keimen
z_c = (960 - mu) / sigma
p_c = 1 - stats.norm.cdf(z_c)

result = {"p_a": p_a, "p_b": p_b, "p_c": p_c}
print(result)