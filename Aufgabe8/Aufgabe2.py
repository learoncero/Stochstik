from scipy.stats import expon

# a)
erwartungswert = 10000
exponentialverteilung = expon(scale = erwartungswert)
ergebnis = exponentialverteilung.ppf(0.5)

print("Die Brenndauer ", ergebnis, " wird mit einer Wahrscheinlichkeit von 50% nicht unterschritten.")


# b)
erwartungswert = 10000
exponentialverteilung = expon(scale = erwartungswert)
wahrsch_mehr_als_10000 = 1 - exponentialverteilung.cdf(10000)

print("Die Wahrscheinlichkeit, dass die Brenndauer mehr als 10000 Stunden beträgt, beträgt ", wahrsch_mehr_als_10000 * 100, "%.")

# c)
erwartungswert = 10000
exponentialverteilung = expon(scale = erwartungswert)
wahrsch_2000_wenn_8500 = 1 - exponentialverteilung.cdf(2000)

print("Die Wahrscheinlichkeit, dass die Brenndauer noch 2000 Stunden beträgt, wenn sie bereits 8500 Stunden betragen hat, beträgt ", wahrsch_2000_wenn_8500 * 100, "%.")