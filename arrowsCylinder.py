from __future__ import division, print_function
from vpython import *

arrz = []
z = -0.1
zmax = 0.11
dz = 0.05
R = 0.1
dtheta = pi/6
while z < zmax:
    theta = 0
    while theta < 2*pi:
        a = arrow(pos=vector(R*cos(theta), R*sin(theta), z),
                  color=color.orange, shaftwidth=0.003,
                  axis=vector(0,0.02,0))
        arrz.append(a)
        theta = theta +dtheta
    z = z + dz

for arr in arrz:
    rate(1)
    arr.axis=vector(0,0,0.02)
    arr.color=color.green
