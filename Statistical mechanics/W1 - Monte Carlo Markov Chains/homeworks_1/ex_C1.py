import random, math
n_trials = 400000
n_hits = 0
var = 0.0
sum_obs_2 = 0
sum_obs = 0
for iter in range(n_trials):
    x, y = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)
    Obs = 0.0
    if x**2 + y**2 < 1.0:
        n_hits += 1
        Obs = 4.0
    sum_obs_2 += Obs**2
    sum_obs += Obs
print(4.0 * n_hits / float(n_trials), math.sqrt(sum_obs_2/n_trials - (sum_obs/n_trials)**2))