import random
import math
import numpy as np
import pylab

n_dimensions =4
delta = 0.1
n_runs = 10
trials_list = [10, 100, 1000, 10000]
v_sph_table = []
err_table = []
for n_trials in trials_list:
    run_res = []
    for _ in range(n_runs):
        prod = 2
        for d in range(1, n_dimensions):
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
                if tot_radius < 1.0: n_hits += 1

            estimated_q = 2 * n_hits / float(n_trials)
            prod *= estimated_q
        run_res.append(prod)
    v_mean = np.mean(run_res)
    v_2_mean = np.mean([t**2 for t in run_res])
    err = math.sqrt((v_2_mean-v_mean**2)/n_runs)
    err_table.append(err)
    v_sph_table.append(v_mean)

def V_sph(dim):
    return math.pi ** (dim / 2.0) / math.gamma(dim / 2.0 + 1.0)

true_v = V_sph(n_dimensions)

import pandas as pd
final_table = pd.DataFrame(
    {'n_trials': trials_list,
     '<V_sph(20)>': v_sph_table,
     'V_sph(20) (exact)': [true_v]*len(trials_list),
     'error': err_table

    })
final_table['difference'] = final_table['<V_sph(20)>']-final_table['V_sph(20) (exact)']
print(final_table)