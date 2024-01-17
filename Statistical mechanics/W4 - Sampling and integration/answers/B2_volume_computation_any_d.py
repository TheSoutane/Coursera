import random
import math
import numpy as np
import pylab

n_dimensions =4
n_trials = 50000
n_hits = 0
delta = 0.1
hist = []

d = n_dimensions-1
x = [0] * d
old_radius_square = 0

def V_sph(dim):
    return math.pi ** (dim / 2.0) / math.gamma(dim / 2.0 + 1.0)

for i in range(n_trials):

    k = random.randint(0, d-1)
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
real_q = V_sph(n_dimensions)/V_sph(n_dimensions-1)

print('estimated: ',estimated_q)
print('real: ',real_q)
print('relative_error%: ', round(abs(estimated_q-real_q)/real_q*100, 0))