import random, math




def direct_disks_box(N, sigma, del_xy, configuration):
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

    min_conf_dist = min(math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) for b in configuration)
    if min_conf_dist<del_xy:
        hit_condition = True
    else:
        hit_condition = False

    return hit_condition

N = 4
sigma = 0.2
n_runs = 100
hit_count = 0
conf_list = ()
del_xy = 0.01
for conf in conf_list:
    for run in range(n_runs):
        hit_count+=direct_disks_box(N, sigma, del_xy, conf)
    print(conf)
    print(hit_count/n_runs)
