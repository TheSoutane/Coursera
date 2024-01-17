import random
import math
import numpy as np
import pylab

n_dimensions = 20
n_trials = 50000
n_hits = 0
delta = 0.1
hist = []

x = [0] * n_dimensions
#import pdb; pdb.set_trace()
old_radius_square = 0

for i in range(n_trials):

    k = random.randint(0, n_dimensions - 1)
    x_old_k = x[k]
    x_new_k = x_old_k + random.uniform(-delta, delta)
    new_radius_square = old_radius_square + x_new_k ** 2 - x_old_k ** 2

    if new_radius_square < 1.0:
        x[k] = x_new_k
        old_radius_square = new_radius_square
    hist.append(math.sqrt(new_radius_square))

pylab.hist(hist, density=True)
x = [a / 100.0 for a in range(0, 101)]
y = [n_dimensions*r**(n_dimensions-1)  for r in x]
pylab.plot(x, y, linewidth=1.5, color='r')
pylab.title('Theoretical distribution $\pi(r)=4*r^3$ and normalized\
    \n histogram for '+str(n_trials)+' samples',fontsize=16)
pylab.savefig(f'illustrative_graph_{n_dimensions}_dim.png')
pylab.show()

