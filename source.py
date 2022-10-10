# source.py - Source Code File (Prefixes, Subscripts, Variables, Units and Formulas)
# By: Joshua Lim
# Date: 10/08/2022
# Modules 1-6 Optimized

# prefixes, subscripts, variables and units
'''

Prefixes:
d = derivative

Subscripts:
f = final
0/i = initial

Variables:
x0 = x-distance initial (y is y0)
v0 = velocity initial
vf = velocity final
a = acceleration
t = time
d = distance
N = normal force
F = force
m = mass
g = gravity (9.81 m/s^2)
Fspring = spring force
k = spring constant
s = spring displacement
s0 = spring displacement initial
w = angular velocity (omega)
r = radius
v = velocity
E = energy
W = work
P = power
h = height
pi = 3.14
p = pressure
vt = velocity tangential
at = acceleration tangential
ac = acceleration centripetal
vc = velocity centripetal

Units:
m = meters
s = seconds
N = newtons
kg = kilograms
T = newtons (for tension)
mu = coefficient of friction - (mu S = static, mu K = kinetic)

'''

# formulas:
'''

0) Basic Algerbra
theta = arctan(y/x)

1) Vector Algebra Formulas:
x-component = x * cos(theta)
y-component = y * sin(theta)
magnitude = sqrt((x-component)^2 + (y-component)^2)
theta = arctan(y/x)
slope = y/x (for graphing)
i1 + j1, i2 + j2 = i1 + i2 + j1 + j2 (for adding vectors)

2) Motion in 1D Formulas:
x = x0 + v0t + 1/2at^2
vf = v0 + at
a = (v - v0) / t
t = (v - v0) / a
v^2 = v0^2 + 2ad
d = v0t + 1/2at^2

3) Projectile Motion (2D) Formulas: (Obojobo Checked)
magnitude = sqrt(vx^2 + vy^2)
angle = degrees(arctan(vy / vx))
v = vxi + vyj - ??
vf = v0 + at
vi,x = v * cos(theta)
vi,y = v * sin(theta) + g * t
h = 1/2 * a * t^2 (free fall)
h = 1/2 * v^2 * sin(2 * theta) / g (projectile)
v = v0 * sin(theta) - g * t
v = sqrt(v0^2 + 2gh)
v^2 = v0^2 + 2gh
range = -(v^2 * sin(2 * theta)) / g
Vy^2 = Vy0^2 + 2a (change in y)
Vx^2 = Vx0^2 + 2a (change in x)

4) Forces Formulas:
F = m * a
F = m * ((vf - v0) / t)
Fspring = k * |s-s0|
F = N * mu K/S
F = T - N * mu K/S
Fs MAX  = muS * Fn
Fs MAX = muS * m * g

5) Newton's Laws of Motion Formulas:
1. A body remains at rest, or in motion at a constant speed in a straight line, unless acted upon by a force.
- F = m * a
2. When a body is acted upon by a force, the time rate of change of its momentum equals the force.
- a = Fnet / m
3. If two bodies exert forces on each other, these forces have the same magnitude but opposite directions.
- Fab = -Fba

6) Circular Motion Formulas:
F = m * ac
F = m * v^2 / r
v^2 / r = w^2 * r
- angular velocity formulas:
w = v / r
w = 2 pi / t
t = 2 pi / w
- centripetal force formulas:
F = m * v^2 / r
F = m * w^2 * r
- centripetal acceleration formulas:
a = v^2 / r
a = w^2 * r
w = v / r
vt = 2 pi r / t
vt = w * r
a = sqrt(ac^2 + at^2)
at = dvt / dt

7) Work and Kinetic Energy Formulas:
W = F * d
W = F * d * cos(theta)
W = 1/2 * m * vf^2 - 1/2 * m * v0^2
W = 1/2 * m * v^2
P = dW / dt
P = F * v
P = F * v * cos(theta)
W = (total change in KE) = 1/2 * m * vf^2 - 1/2 * m * v0^2

8) Conservation of Mechanical Energy Formulas:
PE = mgh 
KE = 1/2 * m * v^2
KEspring = 1/2 * k * s^2
PE0 + KE0 = PEf + KEf
ME = 1/2 * m * v^2 + mgh

9) Linear Momentum and Conservation of Momentum Formulas:


# HAVEN'T DONE YET
10) Collisions and Many Particle Systems Formulas:


11) Torques and Static Equilibrium Formulas:


12) Rotational Motion Formulas:


13) Angular Momentum Formulas:


14) Simple Harmonic Motion Formulas:


15) Waves and Oscillation Formulas:


'''