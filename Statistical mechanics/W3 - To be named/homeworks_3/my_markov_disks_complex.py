import random, math
import pylab
import os
import cmath
import numpy as np

def dist(x, y):
    d_x = abs(x[0] - y[0]) % 1.0
    d_x = min(d_x, 1.0 - d_x)
    d_y = abs(x[1] - y[1]) % 1.0
    d_y = min(d_y, 1.0 - d_y)
    return math.sqrt(d_x ** 2 + d_y ** 2)

def delx_dely(x, y):
    d_x = (x[0] - y[0]) % 1.0
    if d_x > 0.5: d_x -= 1.0
    d_y = (x[1] - y[1]) % 1.0
    if d_y > 0.5: d_y -= 1.0
    return d_x, d_y

def Psi_6(L, sigma):
    # print(L)
    sum_vector = 0j
    for i in range(len(L)):
        vector  = 0j
        n_neighbor = 0
        for j in range(len(L)):
            # import pdb; pdb.set_trace()
            # print(L[i], L[j] )
            if dist(L[i], L[j]) < 2.8 * sigma and i != j:
                n_neighbor += 1
                dx, dy = delx_dely(L[j], L[i])
                angle = cmath.phase(complex(dx, dy))
                vector += cmath.exp(6.0j * angle)
        if n_neighbor > 0:
            vector /= n_neighbor
        sum_vector += vector
    return sum_vector / float(len(L))


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


filename = f'disk_configuration_N{64}_eta{0.72}_steps{10000}.txt'
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

N_disks = 64
N_sq = int(math.sqrt(N_disks))
psi_mean_list = []
eta_list = []
for eta in np.linspace(0.72, 0.2, 20):
# eta = 0.72
    print(eta)
    sigma = math.sqrt(eta/(3.1416*N_disks))
    intra_disk_sigma = 1/N_sq #+ (1-2*N_sq*sigma)
    sigma_sq = sigma ** 2
    # print('verification')
    # print(N_disks*3.1416*sigma_sq-eta)

    L = [[sigma+i*intra_disk_sigma, sigma+j*intra_disk_sigma] for i in range(N_sq) for j in range(N_sq)]
    delta = 0.1
    n_steps = 5000
    Psi_list = []

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
        psi = Psi_6(L, sigma)
        polar = cmath.polar(psi)
        norm_ = polar[0]
        Psi_list.append(norm_)
    eta_list.append(eta)
    psi_mean_list.append(np.mean(Psi_list))
# show_conf(L, sigma, 'test graph V2', '4_disks.png')
# pylab.hist(Psi_list)
pylab.scatter(eta_list, psi_mean_list)
pylab.show()
pylab.close()

# L[0][0] = 3.3
# f = open(filename, 'w')
# for a in L:
#     # print(a[0], a[1])
#     f.write(str(a[0]) + ' ' + str(a[1]) + '\n')
# f.close()