import random, math
def direct_disks_box(N, sigma):
    condition = False
    while condition == False:
        L = [(random.uniform(sigma, 1.0 - sigma), random.uniform(sigma, 1.0 - sigma))]
        for k in range(1, N):
            a = (random.uniform(sigma, 1.0 - sigma), random.uniform(sigma, 1.0 - sigma))
            min_dist = min(math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) for b in L)
            if min_dist < 2.0 * sigma:
                condition = False
                break
            else:
                L.append(a)
                condition = True
    return L


sigma = 0.15
del_xy = 0.1
n_runs = 10000
conf_a = ((0.30, 0.30), (0.30, 0.70), (0.70, 0.30), (0.70,0.70))
conf_b = ((0.20, 0.20), (0.20, 0.80), (0.75, 0.25), (0.75,0.75))
conf_c = ((0.30, 0.20), (0.30, 0.80), (0.70, 0.20), (0.70,0.70))
configurations = [conf_a, conf_b, conf_c]
hits = {conf_a: 0, conf_b: 0, conf_c: 0}
for run in range(n_runs):
    x_vec = direct_disks_box(4, sigma)
    for conf in configurations:
        condition_hit = True
        for b in conf:
            condition_b = min(max(abs(a[0] - b[0]), abs(a[1] - b[1])) for a in x_vec) < del_xy
            condition_hit *= condition_b
        if condition_hit:
            hits[conf] += 1

for conf in configurations:
    print(conf, hits[conf])

# # 10^4
# ((0.3, 0.3), (0.3, 0.7), (0.7, 0.3), (0.7, 0.7))
# 1 - 2 - 2 // 175 - 180 - 178
# ((0.2, 0.2), (0.2, 0.8), (0.75, 0.25), (0.75, 0.75))
# 1 - 2 - 0 // 114 - 111 - 93
# ((0.3, 0.2), (0.3, 0.8), (0.7, 0.2), (0.7, 0.7))
# 0 - 1 - 0 // 114 - 97 - 85

# # 10^5
# ((0.3, 0.3), (0.3, 0.7), (0.7, 0.3), (0.7, 0.7))
# 13 - 14 - 5 // 1881 - 1870 - 1891
# ((0.2, 0.2), (0.2, 0.8), (0.75, 0.25), (0.75, 0.75))
# 7 - 8 - 8 // 918 - 894 - 885
# ((0.3, 0.2), (0.3, 0.8), (0.7, 0.2), (0.7, 0.7))
# 14 - 9 - 19 // 983 - 985 - 961


# # 10^6
# ((0.3, 0.3), (0.3, 0.7), (0.7, 0.3), (0.7, 0.7))
# 100 - 108 - 122 // 19020 - 18865 - 18989
# ((0.2, 0.2), (0.2, 0.8), (0.75, 0.25), (0.75, 0.75))
# 116 - 118 - 136 // 9293 - 9336 - 9375
# ((0.3, 0.2), (0.3, 0.8), (0.7, 0.2), (0.7, 0.7))
# 129 - 121 - 120 // 9962 - 10046 - 9760
