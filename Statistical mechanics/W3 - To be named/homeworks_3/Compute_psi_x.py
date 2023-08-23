import cmath
import math

import pylab
import numpy as np

pi = math.pi

# for t in np.linspace(0.72, 0.2, 10):
#     print(t)


# print(cmath.polar(pi)[0])
vector  = 0
angle_list = [0, pi/3, 2*pi/3, pi, 4*pi/3, 5*pi/3] # 6 +0j
print(np.mean(angle_list))

pylab.hist(angle_list)
pylab.show()
# angle_list = [t + pi/6 for t in angle_list] # -6 +0j
angle_list = [t + math.radians(15) for t in angle_list] # 0 +6j


# angle_list = [0, pi/2, pi, 3*pi/2, 2*pi]

for angle in angle_list:
    complex = cmath.exp(6j * angle)
    vector+=complex
    # print(angle/pi, complex.real, complex.imag)
print(vector.real)
print(vector.imag)

