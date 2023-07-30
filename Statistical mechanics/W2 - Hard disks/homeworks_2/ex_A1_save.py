import random, math




def direct_disks_box(N, sigma):
    condition = False
    while condition == False:
        L = [(random.uniform(sigma, 1.0 - sigma), random.uniform(sigma, 1.0 - sigma))]
        conf_match = True
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

N = 4
sigma = 0.15
n_runs = 100000

conf_a = ((0.3, 0.3), (0.3, 0.7), (0.7, 0.3), (0.7, 0.7))
conf_b = ((0.3, 0.2), (0.3, 0.8), (0.7, 0.2), (0.7, 0.7))
conf_c = ((0.2, 0.2), (0.2, 0.8), (0.75, 0.25), (0.75, 0.75))

count_dict = {conf_a:0,
    conf_b:0,
    conf_c:0
}

del_xy = 0.1

def isin_conf_square(vect, conf, del_xy):
    condition_hit = 1
    for b in conf:
        condition_b = (min(max(abs(a[0] - b[0]), abs(a[1] - b[1])) for a in vect) < del_xy)
        condition_hit *= condition_b

    return condition_hit

for run in range(n_runs):
    hit_count=0
    vect = direct_disks_box(N, sigma)

    for conf in count_dict.keys():
        if isin_conf_square(vect, conf, del_xy):
            count_dict[conf]+=1

for conf in count_dict.keys():
    print(conf)
    print(count_dict[conf])


