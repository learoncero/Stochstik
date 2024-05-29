import numpy as np
from scipy.stats import t

# Daten
qualitaet = [4.50, 4.50, 4.50, 4.00, 4.50, 4.50, 3.50, 4.50, 3.50, 3.00, 4.00, 3.00, 2.00, 2.50, 4.00, 2.00, 2.50, 2.50, 4.00, 3.00]

# Berechnungen
mittelwert = np.mean(qualitaet)
standardabweichung = np.std(qualitaet, ddof=1)
n = len(qualitaet)
mu_0 = 3.817
alpha = 0.05

t_statistic = (mittelwert - mu_0) / (standardabweichung / np.sqrt(n))
kritischer_wert = t.ppf(1-alpha, n-1)

print(f"mittelwert: {mittelwert}")
print(f"standardabweichung: {standardabweichung}")
print(f"n: {n}")
print(f"t_statistic: {t_statistic}")
print(f"kritischer_wert: {kritischer_wert}")