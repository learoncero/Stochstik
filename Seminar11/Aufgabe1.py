from scipy.stats import t

n = 300
x_mean = 12.3
s = 2.7
alpha = 0.05

a = s/(n**0.5)
t_lower_upper = t.ppf(1-alpha/2, n-1)

lower_bound = x_mean - a*t_lower_upper
upper_bound = x_mean + a*t_lower_upper

print(f"Das Konfidenzintervall lautet: [{lower_bound}, {upper_bound}]")