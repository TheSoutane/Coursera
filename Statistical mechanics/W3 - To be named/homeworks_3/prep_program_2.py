import os, random

filename = 'disk_configuration.txt'
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
    print(a[0], a[1])
    f.write(str(a[0]) + ' ' + str(a[1]) + '\n')
f.close()

# Questions:
# 1/ os.path.isfile(filename) Checks if the file corresponding to filename exists
# 2/ The difference between the 2 commands is the action to be performed. In one case, it is to read the file ('r') and in the other case to update/write it ('w')
# 3/ The read function will go through the text file line by line. To separate the elements in the line, we use the .split() function that splits text over a defined string. The defeult value is the space ' '. In this row, the different elements of the line are splitted and attributed to the features a and b
# 4/ Let's go element per element:
# - f.write(: Update the file f
# - str(a[0]) + ' ' + str(a[1]): creates a string object composed of the 1st and 2nd elements of a, separated with a space
# - + '\n': adds a line break
# This program can be used to update values available in a text file. In our case this could be used to store a position history or as a log.