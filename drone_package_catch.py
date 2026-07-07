
import os
os.environ['VPYTHON_LAUNCH_BROWSER'] = 'False'
from vpython import *

scene.center = vec(75,50,0)  # move camera to center the scene

grass = box(pos = vec(75,-10,0), size = vec(600, 3, 70), color = color.green)
pack = sphere(pos = vec(30,200,0), radius = 3, color = color.red, make_trail = True)
drone = sphere(pos = vec(-30,0,0), radius = 5, color = color.cyan, make_trail = True)

pack.v = vec(30, -1, 0)          # Package starting velocity
pack.m = 1.0
pack.p = pack.m * pack.v

drone.m = 2.0                   # drone mass
drone.p = vec(0, 0, 0)          # Starting Momentum
drone.pos = vec(-30, 0, 0)        # Starting position

t = 0
deltat = 0.02

scene.pause()                   # Pauses the simulation so that user can start when ready
# Creating setup for graph that will track how far drone is from the package
graph=gcurve(color=color.purple)

g = vec(0, -9.8, 0)
b = 1.5
# CLEANED RESET FUNCTION: Restores both positions, velocities, trails, and clock state
def reset_simulation():
    global t, running
    running = False    # Stops running physics calculations
    t = 0
    # Reset obs_1 back to initial state
    pack.pos = vec(30, 200, 0)
    pack.p = pack.m * vec(30, -1, 0)
    pack.clear_trail()
    
    # Reset obs_2 back to initial state
    drone.pos = vec(-30, 0, 0)
    drone.p = vec(0, 0, 0)
    drone.clear_trail()
  
    graph.delete()    # CLears old graph data
    running = True

# Create UI Button bound to the reset handler
button(text="Repeat Simulation", bind=reset_simulation)
scene.append_to_caption("\n\n")

while True:
  rate(300)
  if running and pack.pos.y > grass.pos.y:
    t = t + deltat

    Fg_drone = drone.m * g
    Fg_pack = pack.m *g
# Finding the vector 'r' that points from the drone to the package
    r = (pack.pos - drone.pos)      # Updates 'r' each run through loop
    rhat = hat(r)
    magr = mag(r)
# Regulates the drone speed as it approaches the package
    if magr > 20:
        magF_thrust = 250
    else:
        magF_thrust = 250 * (magr / 20)  # Force approaches 0 as magnitude of 'r' approaches 0
    
    F_thrust = magF_thrust * rhat

    drone_v = drone.p / drone.m
    F_drag = -b * drone_v

    Fnet_pack = Fg_pack
    Fnet_drone = F_thrust + Fg_drone + F_drag # Steering thrust AND gravity pulling it down
  
#  MOMENTUM & POSITION UPDATES
    pack.p = pack.p + (Fnet_pack * deltat)
    pack.pos = pack.pos + (pack.p / pack.m) * deltat
    
    drone.p = drone.p + (Fnet_drone * deltat)
    drone.pos = drone.pos + (drone.p / drone.m) * deltat

    graph.plot(t, magr)   # Graph plots how far drone is from package 'r' over time 't'
# Stop and exit from loop if drone goes too fast
    if mag(pack.pos - drone.pos) < 4:
      print(f"The drone caught the package in {t - deltat: .2f} seconds.")
      running = False

print("Loop has finished.")
