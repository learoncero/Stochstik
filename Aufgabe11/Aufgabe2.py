from scipy.stats import norm
import numpy as np

ccm = np.array([197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207])
quantity = np.array([2, 1, 3, 1, 3, 1, 2, 1, 1, 0, 1])
n = np.sum(quantity)
mean = np.average(ccm, weights=quantity)
variance = 2.25
alpha = 0.06

# a)
print(f"Der gewichtete Mittelwert beträgt: {mean}")
print(f"Die Anzahl der Beobachtungen beträgt: {n}")

z_alpha_half = norm.ppf(1 - alpha / 2)
lower = mean - ((variance ** 0.5) / (n ** 0.5)) * z_alpha_half
upper = mean + ((variance ** 0.5) / (n ** 0.5)) * z_alpha_half

print(f"a) Das Konfidenzintervall für den Mittelwert lautet: [{lower}, {upper}]")


# b)
l = 1

n_min = 4 * variance * (z_alpha_half / l) ** 2
n_min = np.ceil(n_min)

print(f"b) Die Anzahl der Beobachtungen, die mindestens benötigt werden, um ein Konfidenzintervall der Breite {l} mit einer Konfidenz von {1-alpha} zu erhalten, beträgt mindestens {n_min}")