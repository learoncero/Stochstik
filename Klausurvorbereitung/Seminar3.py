import numpy as np
from scipy.stats import linregress

# Daten
alter = np.array([4, 7, 11, 2])
bremsweg = np.array([50, 80, 70, 45])

# Lineare Regression
slope, intercept, r_value, p_value, std_err = linregress(alter, bremsweg)

# Gleichung der Regressionsgeraden
regressionsgleichung = f'y = {slope:.2f}x + {intercept:.2f}'

# Korrelationskoeffizient
korrelationskoeffizient = r_value

# Extrapolation für ein 13 Jahre altes Fahrzeug
alter_13 = 13
bremsweg_13 = slope * alter_13 + intercept

regressionsgleichung, korrelationskoeffizient, bremsweg_13