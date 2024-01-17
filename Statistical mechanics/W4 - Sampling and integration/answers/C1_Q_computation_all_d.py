import random
import math
import numpy as np
import pylab

n_dimensions =200
n_trials = 50000
delta = 0.1
q_list = []

for d in range(1, n_dimensions):

    hist = []
    x = [0] * d
    old_radius_square = 0
    n_hits = 0

    for i in range(n_trials):

        k = random.randint(0, d - 1)
        x_old_k = x[k]
        x_new_k = x_old_k + random.uniform(-delta, delta)
        new_radius_square = old_radius_square + x_new_k ** 2 - x_old_k ** 2

        if new_radius_square < 1.0:
            x[k] = x_new_k
            old_radius_square = new_radius_square
        alpha = random.uniform(-1, 1)
        tot_radius = new_radius_square + alpha**2
        hist.append(math.sqrt(new_radius_square))
        if tot_radius < 1.0: n_hits += 1

    estimated_q = 2 * n_hits / float(n_trials)
    q_list.append(estimated_q)
print(np.prod(q_list)*2)

