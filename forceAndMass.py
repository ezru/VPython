from __future__ import division
from vpython import *
scene.width = 800
scene.height = 600

#constant
k = 0.1
a = 1
L0 = 1.9
m = 0.001
g = 9.8
scaleFactor = 100

#objects
floor = box(length=5, width=1, height=0.1, color=color.green)
wall = box(pos=vector(-floor.length/2+0.05,0.5+floor.height/2,0), length=0.1, width=1, height=1, color = color.green)
mass = box(pos=vector(0,a/2+floor.height/2,0), length=a, width=a, height=a, color=color.white, opacity=0.5)
spring = helix(pos=wall.pos + vector(wall.length/2,0,0), axis = mass.pos -vector(0.5,0,0) - wall.pos, radius=0.2, color = color.green)

#Claculations
L = spring.axis
s = mag(L) - L0
L_hat = L/mag(L)
Fspring = -k*s*L_hat
Fgrav = m*g*vector(0,-1,0)

#Force Arrow
Fspring_arr = arrow(pos=mass.pos, axis=Fspring*scaleFactor, color=color.red)
Fgrav_arr = arrow(pos=mass.pos, axis=Fgrav*scaleFactor, color=color.red)

print("Spring Force = ", Fspring)
print("wall.pos - mass.pos", wall.pos - mass.pos)
