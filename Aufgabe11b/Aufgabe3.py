from scipy.stats import t

# a)
mean = 1.66
s = 0.04
n = 10
alpha = 0.1

t_val = t.ppf(1 - alpha / 2, df=n-1)
lower = mean - t_val * (s / n ** 0.5)
upper = mean + t_val * (s / n ** 0.5)
print(f"a) Das Konfidenzintervall für den Mittelwert lautet: [{lower}, {upper}]")