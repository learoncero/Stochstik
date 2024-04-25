from scipy.stats import norm

sigma = 1.5

# Das 99%-Perzentil berechnen, da wir wollen, dass nur 1% der Fälle überfließen (100% - 99% = 1%)
value = norm.ppf(0.99, loc=0, scale=sigma)

# Der Mittelwert mu, auf den der Automat eingestellt werden muss, ist 25 cl minus das 99%-Perzentil
mu = 25 - value
print(f"Der Automat muss auf einen Mittelwert von {mu} cl eingestellt werden, damit nur 1% der Tassen überfließen.")