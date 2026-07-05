
import os
os.environ['VPYTHON_LAUNCH_BROWSER'] = 'False'

from vpython import *

scene.center = vec(75,50,0)  # move camera to center the scene

grass = box(pos = vec(75,-10,0), size = vec(600, 3, 70), color = color.green)
pack = sphere(pos = vec(30,200,0), radius = 3, color = color.red, make_trail = True)
drone = sphere(pos = vec(-20,0,0), radius = 5, color = color.cyan, make_trail = True)

pack.v = vec(20, -1, 0)          # Package starting velocity
pack.m = 1.0
pack.p = pack.m * pack.v

drone.m = 2.0                   # drone mass
drone.p = vec(0, 0, 0)          # Starting Momentum
drone.pos = vec(-20, 0, 0)        # Starting position

t = 0
deltat = 0.05

scene.pause()                   # Pauses the simulation so that user can start when ready

# Creating setup for graph that will track how far drone is from the package
graph=gcurve(color=color.purple)

g = vec(0, -9.8, 0)
b = 1.5

while pack.pos.y > grass.pos.y:
  rate(300)

  t = t + deltat

  Fg_drone = drone.m * g
  Fg_pack = pack.m *g

# Finding the vector 'r' that points from the drone to the package
  r = (pack.pos - drone.pos)      # Updates 'r' each run through loop
  rhat = hat(r)
  magr = mag(r)

# Regulates the drone speed as it approaches the package
  if magr > 10:
      magF_thrust = 60

  else:
      magF_thrust = 60 * (magr / 10)  # Force approaches 0 as magnitude of 'r' approaches 0

  F_thrust = magF_thrust * rhat

  drone_v = drone.p / drone.m
  F_drag = -b * drone_v

  Fnet_pack = Fg_pack
  Fnet_drone = F_thrust + Fg_drone + F_drag # Steering thrust AND gravity pulling it down
  
#  MOMENTUM UPDATES
  pack.p = pack.p + (Fnet_pack * deltat)
  drone.p = drone.p + (Fnet_drone * deltat)

#  POSITION UPDATES
  pack.pos = pack.pos + (pack.p / pack.m) * deltat
  drone.pos = drone.pos + (drone.p / drone.m) * deltat

  graph.plot(t, magr)   # Graph plots how far drone is from package 'r' over time 't'

# Stop and exit from loop if drone goes too fast
  if mag(pack.pos - drone.pos) < 3:
    print(f"The drone caught the package in {t - deltat: .2f} seconds.")
    break

print("Loop has finished.")
