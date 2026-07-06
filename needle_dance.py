import os
os.environ['VPYTHON_LAUNCH_BROWSER'] = 'False'

from vpython import *

scene.background = color.white 

# the following two lines draw axes
xaxis = curve(pos=[vec(-0.9, 0, 0), vec(0.9, 0, 0)], color=color.gray(0.5))
yaxis = curve(pos=[vec(0,0-0.3, 0), vec(0, 0.3, 0)], color=color.gray(0.5))
L = 0.25                # length of rod 
Q = 2e-8                #Rod total Charge

sphereQ = -3.3e-10
t=0

a = cylinder(pos=vec(-L/2, 0, 0), axis=vec(L,0,0), radius=0.003, opacity=0.3)
N = 40                         #Segments of Rod
seg = L/N                      #Size of Rod Segments
spherePoint = (-L/2) + seg/2   #Location where each sphere should go
dQ = Q/N                       #Charge of each segment


while spherePoint < .95 * (L/2):
  sphere(pos=vec(spherePoint,0,0), radius=0.0025, color=color.red)
  spherePoint = spherePoint + seg

dx = L/N    		         #Change in X
x = -L/2 + (dx/2)
dt = 0.01

obs_1 = sphere(pos=vec(0.1, 0.015, 0), radius=0.003, color=color.blue, visible=True, vel=vec(0, 0,0.088))
obs_2 = sphere(pos=vec(-0.1, -0.015, 0), radius=0.003, color=color.blue, visible=True, vel=vec(0, 0,-0.088))

while t < 100:
  rate(60)
  fieldE_1 = vec(0,0,0)
  fieldE_2 = vec(0,0,0)

  x = -L/2 + (dx/2)

# Function that resets the test charge back to its starting state
def reset_simulation():
    global t, k
    t = 0
    k = vec(0, 0, 0)
    test_charge.pos = vec(0, R, 0)
    test_charge.clear_trail()  # Clears the old line from the screen
    print("Simulation reset!")

# Create the clickable button in the browser canvas
button(text = "Repeat Simulation", bind = reset_simulation)
scene.append_to_caption("\n\n") # Adds vertical spacing below the button
  
  while x < L/2:
    segmentpos = vec(x,0,0)     ## don't make a sphere, just use the position
    r_1 = obs_1.pos - segmentpos
    r_2 = obs_2.pos - segmentpos
    fieldNewE_1 = 9e9 * (dQ / mag(r_1)**2) * hat(r_1)
    fieldE_1 = fieldE_1 + fieldNewE_1

    fieldNewE_2 = 9e9 * (dQ / mag(r_2)**2) * hat(r_2)
    fieldE_2= fieldE_2 + fieldNewE_2

    x = x + dx

  force_1 = fieldE_1 * sphereQ
  acceleration_1 = force_1 / 0.0001
  obs_1.vel = obs_1.vel + (acceleration_1 * dt)
  obs_1.pos = obs_1.pos + (obs_1.vel *dt)

  force_2 = fieldE_2 * sphereQ
  acceleration_2 = force_2 / 0.0001
  obs_2.vel = obs_2.vel + (acceleration_2 * dt)
  obs_2.pos = obs_2.pos + (obs_2.vel *dt)

  t = t + dt

