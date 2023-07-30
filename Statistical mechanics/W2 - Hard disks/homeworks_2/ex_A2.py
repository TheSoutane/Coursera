import random, math
L = [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]]
sigma = 0.15
sigma_sq = sigma ** 2
delta = 0.1

sigma = 0.15
del_xy = 0.1
conf_a = ((0.30, 0.30), (0.30, 0.70), (0.70, 0.30), (0.70,0.70))
conf_b = ((0.20, 0.20), (0.20, 0.80), (0.75, 0.25), (0.75,0.75))
conf_c = ((0.30, 0.20), (0.30, 0.80), (0.70, 0.20), (0.70,0.70))
configurations = [conf_a, conf_b, conf_c]
hits = {conf_a: 0, conf_b: 0, conf_c: 0}

def Markov_disks_boxs(L, n_steps, delta, sigma, configurations, hits):
    for steps in range(n_steps):
        a = random.choice(L)
        b = [a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta)]
        min_dist = min((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2 for c in L if c != a)
        box_cond = min(b[0], b[1]) < sigma or max(b[0], b[1]) > 1.0 - sigma
        if not (box_cond or min_dist < 4.0 * sigma ** 2):
            a[:] = b
        for conf in configurations:
            condition_hit = True
            for b in conf:
                condition_b = min(max(abs(a[0] - b[0]), abs(a[1] - b[1])) for a in L) < del_xy
                condition_hit *= condition_b
            if condition_hit:
                hits[conf] += 1
    return hits

n_steps = 10000
hits = Markov_disks_boxs(L, n_steps, delta, sigma, configurations, hits)

for conf in configurations:
    print(conf, hits[conf])

# 10^4
# ((0.3, 0.3), (0.3, 0.7), (0.7, 0.3), (0.7, 0.7))
# 0 - 0 - 0 // 164 - 139 - 152
# ((0.2, 0.2), (0.2, 0.8), (0.75, 0.25), (0.75, 0.75))
# 1 - 0 - 0 // 85 - 79 - 56
# ((0.3, 0.2), (0.3, 0.8), (0.7, 0.2), (0.7, 0.7))
# 0 - 0 - 0 // 103 - 68 - 53

# 10^5
# ((0.3, 0.3), (0.3, 0.7), (0.7, 0.3), (0.7, 0.7))
# 8 - 6 - 9 // 1907 - 2097 - 2026 - 2124
# ((0.2, 0.2), (0.2, 0.8), (0.75, 0.25), (0.75, 0.75))
# 26 - 25 - 25 // 1002 - 1018 - 1094 - 891
# ((0.3, 0.2), (0.3, 0.8), (0.7, 0.2), (0.7, 0.7))
# 25 - 14 - 9 // 1054 - 1148 - 1039 - 1103

# 10^6
# ((0.3, 0.3), (0.3, 0.7), (0.7, 0.3), (0.7, 0.7))
# 124 - 94 - 107 //1853 - 19390 - 18806
# ((0.2, 0.2), (0.2, 0.8), (0.75, 0.25), (0.75, 0.75))
# 100 - 136 - 94 // 9292 - 8962 - 10213
# ((0.3, 0.2), (0.3, 0.8), (0.7, 0.2), (0.7, 0.7))
# 128 - 109 - 97 // 9973 - 10609 - 9882