from scipy.stats import t

n = 50

# a)
alpha = 0.05
goals = [0, 1, 2, 3, 4]
num_of_games = [18, 22, 5, 3, 2]

mean = sum([goals[i] * num_of_games[i] for i in range(len(goals))]) / n
variance = sum([num_of_games[i] * (goals[i] - mean) ** 2 for i in range(len(goals))]) / (n - 1)

t_val = t.ppf(1 - alpha / 2, df=n-1)
lower = mean - t_val * (variance / n) ** 0.5
upper = mean + t_val * (variance / n) ** 0.5

print(f"a) Das Konfidenzintervall für den Mittelwert lautet: [{lower}, {upper}]")