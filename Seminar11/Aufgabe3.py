from scipy.stats import t

n = 64
x_mean = 75
s = 8
alpha = 0.1

a = s/(n**0.5)
t_lower_upper = t.ppf(1-alpha/2, n-1)

lower_bound = x_mean - a*t_lower_upper
upper_bound = x_mean + a*t_lower_upper

print(f"Das Konfidenzintervall lautet: [{lower_bound}, {upper_bound}]")