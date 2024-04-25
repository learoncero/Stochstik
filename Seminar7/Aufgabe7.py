from scipy.stats import poisson

lambda_value = 8000
availability_target = 0.97

num_tables_year = poisson.isf(availability_target, lambda_value)
num_tables_day = num_tables_year / 365
num_tables_hour = num_tables_day / 4   

print(num_tables_hour)