import os
os.environ['VPYTHON_LAUNCH_BROWSER'] = 'False'

from vpython import *

scene.center = vec(75,50,0)  

grass = box(pos = vec(75,-10,0), size = vec(400,3,70), color=color.green)
pack = sphere(pos=vec(50,100,0), radius=3, color=color.red, make_trail = True)
drone = sphere(pos=vec(0,0,0), radius=5, color = color.cyan, make_trail = True)

pack.v = vec(2,-1,0)

drone.m = 2.0        
drone.pos = vec(0,0,0)
drone.p = vec(0,0,0)  # FIX: Defined initial momentum so the physics update works!

t = 0
deltat = 0.05

scene.pause()

graph = gcurve(color=color.purple)

while pack.pos.y > grass.pos.y:
  rate(300)
  t = t + deltat
  r = (pack.pos - drone.pos)

  rhat = hat(r)
  magr = mag(r)
  
  # Note: A constant Fnet of (150, 100, 0) means the drone will accelerate in a straight line,
  # rather than turning to follow the package. 
  Fnet = 10 * rhat
  
  pack.pos = pack.pos + pack.v * deltat
  drone.p = drone.p + (Fnet * deltat)
  drone.pos = drone.pos + (drone.p / drone.m) * deltat
  
  graph.plot(t, magr)

  # Check top speed
  if mag(drone.p / drone.m) > 9:
    print(f"The drone exceeded its top speed at {t: .2f} seconds.")
    break
    
  # Check intercept condition
  if mag(pack.pos - drone.pos) < 3:
    # Cleaned up variation of your print statement rounded neatly to 2 decimal places
    print(f"The drone caught the package in {t: .2f} seconds.")
    break

print("Loop has finished.")
