import numpy as np
from scipy.stats import norm

fill_amounts = [499.7, 501.3, 499.1, 500.6, 500.2, 499.5, 500.0, 499.1, 500.5, 499.6, 498.7, 501.7]
n = len(fill_amounts)
mean_fill = np.mean(fill_amounts)
sigma = 1

# a)
alpha = 0.01
z = norm.ppf(1 - alpha/2)
ci_lower = mean_fill - z * (sigma / np.sqrt(n))
ci_upper = mean_fill + z * (sigma / np.sqrt(n))

print(f"a) Das Konfidenzintervall für den Mittelwert lautet: [{ci_lower}, {ci_upper}]")

# b)
l = 0.5
alpha = 0.01

n_min = 4 * sigma**2 * z**2 / l**2
n_min = np.ceil(n_min)

print(f"b) Die Anzahl der Füllungen, die mindestens benötigt werden, um ein Konfidenzintervall der Breite {l} mit einer Konfidenz von {1-alpha} zu erhalten, beträgt mindestens {n_min}")