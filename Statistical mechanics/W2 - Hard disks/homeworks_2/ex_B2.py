import random, pylab

def Markov_disks_boxs(L, n_steps, delta, sigma):
    histo_data = []
    for steps in range(n_steps):
        a = random.choice(L)
        b = [a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta)]
        min_dist = min((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2 for c in L if c != a)
        box_cond = min(b[0], b[1]) < sigma or max(b[0], b[1]) > 1.0 - sigma
        if not (box_cond or min_dist < 4.0 * sigma ** 2):
            a[:] = b
        for k in range(len(L)):
            histo_data.append(L[k][0])

    return histo_data

n_steps = 2000000
L = [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]]
sigma = 0.15
sigma_sq = sigma ** 2
delta = 0.1

sigma = 0.15
del_xy = 0.1
histo_data = Markov_disks_boxs(L, n_steps, delta, sigma)

pylab.hist(histo_data, bins=100)
pylab.xlabel('x')
pylab.ylabel('frequency')
pylab.title('Direct sampling: x coordinate histogram (density eta=0.18)')
pylab.grid()
pylab.savefig('Markov_disks_histo.png')
pylab.show()