import numpy as np
from scipy.stats import pearsonr
import pandas as pd

# Beispiel Daten
data = {
    "HarvestTime": [
    12.00, 10.00, 10.00, 9.00, 8.00, 9.00, 9.00, 7.00, 8.00, 25.00,
    15.00, 11.00, 23.00, 22.00, 21.00, 23.00, 22.00, 22.00, 13.00, 24.00,
    24.00, 21.00, 20.00, 20.00, 10.00, 13.00, 19.00, 23.00, 20.00, 21.00,
    12.00, 19.00, 19.00, 20.00, 20.00, 18.00, 14.00, 13.00, 18.00, 17.00,
    11.00, 19.00, 18.00, 21.00, 18.00, 15.00, 23.00, 22.00, 13.00, 12.00,
    15.00, 24.00, 15.00, 16.00, 13.00, 20.00, 24.00, 25.00, 22.00, 11.00,
    12.00, 10.00, 16.00, 10.00, 22.00, 19.00, 16.00, 11.00, 16.00, 21.00,
    14.00, 22.00, 17.00, 17.00, 16.00, 15.00, 23.00, 16.00, 16.00, 14.00,
    14.00, 12.00, 14.00, 12.00, 13.00, 13.00, 13.00, 12.00, 21.00, 12.00,
    11.00, 11.00, 11.00, 10.00, 21.00, 20.00, 15.00, 13.00, 20.00, 20.00,
    10.00, 25.00, 13.00, 16.00, 17.00, 10.00, 19.00, 16.00, 21.00, 23.00,
    19.00, 18.00, 17.00, 20.00, 20.00, 25.00, 23.00, 12.00, 16.00, 23.00,
    18.00, 24.00, 19.00, 21.00, 10.00, 24.00, 14.00, 19.00, 15.00, 11.00,
    20.00, 22.00, 11.00, 11.00, 14.00, 23.00, 17.00, 7.00, 22.00, 10.00,
    7.00, 7.00, 7.00, 6.00, 7.00, 21.00, 23.00, 18.00, 5.00, 6.00, 6.00,
    14.00, 21.00, 6.00, 18.00, 5.00, 5.00, 6.00, 11.00, 5.00, 5.00, 5.00,
    18.00, 20.00, 4.00, 4.00, 20.00, 23.00, 15.00, 23.00, 19.00, 11.00,
    10.00, 12.00, 22.00, 11.00, 11.00, 15.00, 12.00, 12.00, 22.00, 17.00,
    18.00, 22.00, 12.00, 16.00, 17.00, 14.00, 15.00, 18.00, 17.00, 10.00,
    17.00, 17.00, 14.00, 11.00, 10.00, 16.00, 15.00, 15.00, 15.00, 14.00,
    21.00, 13.00, 14.00, 14.00, 13.00, 25.00, 12.00, 11.00, 11.00, 11.00,
    16.00, 11.00, 11.00, 11.00, 12.00, 18.00, 12.00, 15.00, 10.00, 10.00,
    9.00, 9.00, 13.00, 11.00, 9.00, 8.00, 22.00, 8.00, 19.00, 25.00, 17.00,
    17.00, 19.00, 8.00, 22.00, 15.00, 11.00, 25.00, 15.00
],
    "Brix": [
    9.00, 9.50, 12.50, 9.00, 9.00, 9.50, 10.00, 10.50, 10.50, 7.00,
    11.10, 14.20, 5.50, 7.00, 10.50, 6.50, 6.00, 6.50, 14.10, 6.50,
    6.00, 7.00, 10.50, 9.50, 15.90, 13.20, 11.00, 11.50, 7.50, 8.50,
    10.20, 8.00, 9.00, 7.50, 8.50, 8.50, 10.60, 11.40, 8.50, 7.00,
    13.70, 10.90, 9.00, 10.20, 10.00, 14.30, 10.60, 11.10, 10.90, 11.50,
    14.00, 16.00, 11.90, 11.40, 15.10, 11.00, 10.00, 10.40, 14.20, 11.50,
    14.60, 14.70, 13.70, 10.00, 12.20, 11.30, 7.40, 11.00, 8.30, 8.00,
    12.70, 10.40, 8.00, 9.50, 8.00, 11.00, 11.30, 9.00, 10.50, 10.00,
    9.50, 11.50, 11.10, 11.50, 10.00, 10.00, 11.50, 10.50, 12.60, 10.50,
    12.00, 12.00, 9.00, 12.00, 11.80, 11.20, 12.40, 11.00, 7.00, 12.40,
    8.10, 9.10, 8.20, 8.10, 6.30, 9.90, 6.60, 6.90, 6.30, 7.70, 8.50,
    8.60, 6.50, 8.50, 7.40, 6.70, 6.60, 6.80, 6.70, 9.80, 7.40, 9.10,
    7.50, 8.60, 7.30, 7.70, 9.30, 7.60, 9.10, 6.20, 7.20, 9.00, 9.80,
    8.60, 8.00, 9.20, 6.40, 14.00, 8.70, 7.00, 13.50, 12.00, 13.00, 13.00,
    14.00, 6.10, 6.70, 6.80, 13.50, 13.50, 13.00, 8.40, 9.10, 13.50, 6.70,
    12.50, 14.00, 14.50, 8.10, 14.00, 14.00, 15.00, 8.60, 9.10, 14.00, 14.50,
    12.70, 14.10, 15.20, 15.00, 12.70, 14.60, 15.20, 12.40, 14.00, 13.90,
    12.50, 15.80, 14.20, 13.40, 13.20, 14.60, 15.10, 14.50, 14.10, 15.40,
    12.80, 14.30, 14.30, 7.50, 8.00, 12.00, 12.50, 14.80, 10.50, 14.10,
    13.40, 8.50, 7.50, 8.00, 12.50, 12.00, 13.00, 13.00, 11.00, 13.10,
    15.70, 12.40, 11.00, 11.50, 10.00, 14.80, 14.90, 12.00, 12.00, 11.00,
    14.80, 14.00, 12.00, 13.70, 8.50, 10.00, 8.00, 12.00, 12.80, 16.00,
    10.00, 11.50, 14.90, 11.50, 14.40, 14.30, 15.60, 14.50, 13.90, 11.00,
    14.00, 12.10, 15.40, 13.60, 14.50
]
}

# Daten in ein DataFrame umwandeln
df = pd.DataFrame(data)

# Pearson-Korrelationskoeffizient berechnen
corr, p = pearsonr(df['HarvestTime'], df['Brix'])

print(f'Pearson-Korrelationskoeffizient: {corr}')
print(f'p-Wert: {p}')

# Ergebnis interpretieren
alpha = 0.05
if p < alpha:
    print('Ablehnung der Nullhypothese: Es gibt einen signifikanten Zusammenhang zwischen der Erntezeit und der Süße.')
else:
    print('Annahme der Nullhypothese: Es gibt keinen signifikanten Zusammenhang zwischen der Erntezeit und der Süße.')
