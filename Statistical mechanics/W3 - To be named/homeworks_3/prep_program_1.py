import pylab
def show_conf(L, sigma, title, fname):
    pylab.axes()
    for [x, y] in L:
        for ix in range(-1, 2):
            for iy in range(-1, 2):
                print(ix, iy)
                cir = pylab.Circle((x + ix, y + iy), radius=sigma,  fc='r')
                print(cir)
                
                pylab.gca().add_patch(cir)
    pylab.axis('scaled')
    pylab.title(title)
    pylab.axis([0.0, 1.0, 0.0, 1.0])
    pylab.savefig(fname)
    pylab.show()
    pylab.close()

L = [[0.9, 0.9]]
sigma = 0.4
show_conf(L, sigma, 'test graph', 'one_disk.png')

# Questions:
# 1/It draws a circle. The periodic boundaries create these surprising shape
# 2/ The object color is red. It is specified here:  fc='r'. 'fc' is the ... parameter
# 3/ The periodic boundary condition are implemented using ...
# 4/ The pylab command pylab.show() makes the figure visible on the computer screen. We would need to go to the saved file otherwise
# 5/ The row "pylab.savefig(fname)" creates a file. To change the naming, one would need to modify the fine name in the input function (last row)