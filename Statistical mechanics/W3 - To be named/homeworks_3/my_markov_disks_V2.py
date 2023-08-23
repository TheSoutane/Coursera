import random, math
import pylab

def dist(x, y):
    d_x = abs(x[0] - y[0]) % 1.0
    d_x = min(d_x, 1.0 - d_x)
    d_y = abs(x[1] - y[1]) % 1.0
    d_y = min(d_y, 1.0 - d_y)
    return math.sqrt(d_x ** 2 + d_y ** 2)


def show_conf(L, sigma, title, fname):
    pylab.axes()
    for [x, y] in L:
        for ix in range(-1, 2):
            for iy in range(-1, 2):
                # print(ix, iy)
                cir = pylab.Circle((x + ix, y + iy), radius=sigma, fc='r')
                # print(cir)

                pylab.gca().add_patch(cir)
    pylab.axis('scaled')
    pylab.title(title)
    pylab.axis([0.0, 1.0, 0.0, 1.0])
    pylab.savefig(fname)
    pylab.show()
    pylab.close()


L = [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]]

eta = 0.5
sigma = math.sqrt(eta/(3.1416*len(L)))

sigma_sq = sigma ** 2
print('verification')
print(len(L)*3.1416*sigma_sq-eta)

delta = 0.1
n_steps = 1000
for steps in range(n_steps):
    a = random.choice(L)
    b = [(a[0] + random.uniform(-delta, delta))%1.0, (a[1] + random.uniform(-delta, delta))%1.0]
    dist_list = [dist(b, c) for c in L if c != a]
    print(dist_list)
    min_dist = min(dist_list)
    print(min_dist)
    # box_cond = min(b[0], b[1]) < sigma or max(b[0], b[1]) > 1.0 - sigma
    if min_dist > 2 * sigma:
        print('accepted')
        a[:] = b

show_conf(L, sigma, 'test graph V2', '4_disks.png')

