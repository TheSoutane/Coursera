import random, math
import pylab
import os

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


N_disks = 64
N_sq = int(math.sqrt(N_disks))
eta = 0.72
sigma = math.sqrt(eta/(3.1416*N_disks))
intra_disk_sigma = 1/N_sq #+ (1-2*N_sq*sigma)
sigma_sq = sigma ** 2
print('verification')
print(N_disks*3.1416*sigma_sq-eta)


L = [[sigma+i*intra_disk_sigma, sigma+j*intra_disk_sigma] for i in range(N_sq) for j in range(N_sq)]
delta = 0.1
n_steps = 1000
for steps in range(n_steps):
    a = random.choice(L)
    b = [(a[0] + random.uniform(-delta, delta))%1.0, (a[1] + random.uniform(-delta, delta))%1.0]
    dist_list = [dist(b, c) for c in L if c != a]
    # print(dist_list)
    min_dist = min(dist_list)
    # print(min_dist)
    # box_cond = min(b[0], b[1]) < sigma or max(b[0], b[1]) > 1.0 - sigma
    if min_dist > 2 * sigma:
        print('accepted')
        a[:] = b

show_conf(L, sigma, 'test graph V2', '4_disks.png')

filename = f'disk_configuration_N{len(L)}_eta{eta}.txt'
if os.path.isfile(filename):
    f = open(filename, 'r')
    L = []
    for line in f:
        # print(line, line.split())
        a, b = line.split()
        L.append([float(a), float(b)])
    f.close()
    print('starting from file', filename)
else:
    L = []
    for k in range(3):
        L.append([random.uniform(0.0, 1.0), random.uniform(0.0, 1.0)])
    print('starting from a new random configuration')

L[0][0] = 3.3
f = open(filename, 'w')
for a in L:
    # print(a[0], a[1])
    f.write(str(a[0]) + ' ' + str(a[1]) + '\n')
f.close()