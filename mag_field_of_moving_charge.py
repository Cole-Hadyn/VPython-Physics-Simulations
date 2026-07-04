# This allows the simulation to be opened in the browser
import os
os.environ['VPYTHON_LAUNCH_BROWSER'] = 'False'

from vpython import *

mnofp= 1e-7  # mu_0 / 4pi

# Particle parameters
particle = sphere(pos=vec(-10e-7, 0, 0), radius=2e-8, color=color.red)
q = 1.602e-19
particle.v = vector(2e3, 0, 0)

# 1st obs parameters
obs1 = sphere(pos=vec(0, 0, 2e-7), radius=2e-8, color=color.orange, B= vector(0,0,0), visible=False)
r1 = obs1.pos - particle.pos
rhat1 = hat(r1)
c1 = cross(particle.v, rhat1)
obs1.B = (mnofp*(q*(c1/(mag(r1)**2))))
print("obs1 B=", obs1.B)
attach_arrow(obs1, "B", scale=5e4, shaftwidth = obs1.radius)

# 2nd obs parameters
obs2 = sphere(pos=vec(0, 0, -2e-7), radius=2e-8, color=color.orange, B= vector(0,0,0), visible=False)
r2 = obs2.pos - particle.pos
rhat2 = hat(r2)
c2 = cross(particle.v, rhat2)
obs2.B = (mnofp*(q*(c2/(mag(r2)**2))))
print("obs2 B=", obs2.B)
attach_arrow(obs2, "B", scale=5e4, shaftwidth = obs2.radius)

# 3rd obs parameters
obs3 = sphere(pos=vec(0, 2e-7, 0), radius=2e-8, color=color.orange, B= vector(0,0,0), visible=False)
r3 = obs3.pos - particle.pos
rhat3 = hat(r3)
c3 = cross(particle.v, rhat3)
obs3.B = (mnofp*(q*(c3/(mag(r3)**2))))
print("obs3 B=", obs3.B)
attach_arrow(obs3, "B", scale=5e4, shaftwidth = obs3.radius)

# 4th obs parameters
obs4 = sphere(pos=vec(0, -2e-7, 0), radius=2e-8, color=color.orange, B= vector(0,0,0), visible=False)
r4 = obs4.pos - particle.pos
rhat4 = hat(r4)
c4 = cross(particle.v, rhat4)
obs4.B = (mnofp*(q*(c4/(mag(r4)**2))))
print("obs4 B=", obs4.B)
attach_arrow(obs4, "B", scale=5e4, shaftwidth = obs4.radius)

# 5th obs parameters
obs5 = sphere(pos=vec(2e-7, 0, 0), radius=2e-8, color=color.orange, B= vector(0,0,0), visible=False)
r5 = obs5.pos - particle.pos
rhat5 = hat(r5)
c5 = cross(particle.v, rhat5)
obs5.B = (mnofp*(q*(c5/(mag(r5)**2))))
print("obs5 B=", obs5.B)
attach_arrow(obs5, "B", scale=5e4, shaftwidth = obs5.radius)

# 6th obs parameters
obs6 = sphere(pos=vec(-2e-7, 0, 0), radius=2e-8, color=color.orange, B= vector(0,0,0), visible=False)
r6 = obs6.pos - particle.pos
rhat6 = hat(r6)
c6 = cross(particle.v, rhat6)
obs6.B = (mnofp*(q*(c6/(mag(r6)**2))))
print("obs6 B=", obs6.B)
attach_arrow(obs6, "B", scale=5e4, shaftwidth = obs6.radius)

print("Starting observations")

dt = 1e-12
t = 0

step_count = 0
data_set = 0

scene.range = 1.2e-6

while t < 1.5e-9:
  rate(100)
  particle.pos = particle.pos + particle.v * dt
  t = t + dt
  step_count = step_count + 1

  r1 = obs1.pos - particle.pos
  c1 = cross(particle.v, hat(r1))
  obs1.B = (mnofp*(q*(c1/(mag(r1)**2))))	# Magnetic field at observation pt.
  
  r2 = obs2.pos - particle.pos
  c2 = cross(particle.v, hat(r2))
  obs2.B = (mnofp*(q*(c2/(mag(r2)**2))))
  
  r3 = obs3.pos - particle.pos
  c3 = cross(particle.v, hat(r3))
  obs3.B = (mnofp*(q*(c3/(mag(r3)**2))))
  
  r4 = obs4.pos - particle.pos
  c4 = cross(particle.v, hat(r4))
  obs4.B = (mnofp*(q*(c4/(mag(r4)**2))))
  
  r5 = obs5.pos - particle.pos
  c5 = cross(particle.v, hat(r5))
  obs5.B = (mnofp*(q*(c5/(mag(r5)**2))))

  r6 = obs6.pos - particle.pos
  c6 = cross(particle.v, hat(r6))
  obs6.B = (mnofp*(q*(c6/(mag(r6)**2))))

  if step_count % 100 ==0:
    print("obs1 B=", obs1.B)
    print("obs2 B=", obs2.B)
    print("obs3 B=", obs3.B)
    print("obs4 B=", obs4.B)
    print("obs5 B=", obs5.B)
    print("obs6 B=", obs6.B)
    data_set = data_set + 1
    print("Collected dataset:", data_set)
# Had to change the variables used for r value, and cross products to update the mag field
# Obs on x-axis had a mag field of 0; This is becuase the cross product of two vectors in the same direction is 0.
# Largest mag field is when the particle is closest to a obs location
