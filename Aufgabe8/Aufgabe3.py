from scipy.stats import norm

sigma = 1.5



# 99%-Perzentil berechnen, da wir wollen, dass nur 1% der Fälle überfließen (100% - 99% = 1%)
z_value = norm.ppf(0.99)
print(f"Der Z-Wert beträgt {z_value}.")

# Der Mittelwert mu, auf den der Automat eingestellt werden muss, ist 25 cl minus das 99%-Perzentil
value = z_value * sigma
mu = 25 - value
print(f"Der Automat muss auf einen Mittelwert von {mu} cl eingestellt werden, damit nur 1% der Tassen überfließen.")