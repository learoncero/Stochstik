import math

sigma = 3
n = 300
z = 1.96
mean_x = 12.3

# Standard error
SE = sigma / math.sqrt(n)

# Confidence interval
lower_bound = mean_x - z * SE
upper_bound = mean_x + z * SE

print(lower_bound, upper_bound)