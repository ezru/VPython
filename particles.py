from __future__ import division, print_function
from vpython import *

s1 = sphere(pos=vector(-2,-2,-2), color=color.green)
s2 = sphere(pos=vector(-2,-2,2), color=color.green)
s3 = sphere(pos=vector(-2,2,2), color=color.green)
s4 = sphere(pos=vector(-2,2,-2), color=color.green)
s5 = sphere(pos=vector(2,-2,-2), color=color.green)
s6 = sphere(pos=vector(2,-2,2), color=color.green)
s7 = sphere(pos=vector(2,2,-2), color=color.green)
s8 = sphere(pos=vector(2,2,2), color=color.green)

particles = [s1, s2, s3, s4, s5, s6, s7, s8]

i=0

while i<len(particles):
    rate(1)
    print("particle", i, "pos:",particles[i].pos)
    particles[i].color=color.blue
    i = i + 1
