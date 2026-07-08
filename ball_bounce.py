import os
os.environ['VPYTHON_LAUNCH_BROWSER'] = 'False'

from vpython import *

'''
  create the screen, this makes it easier to see things
'''
my_world = canvas(title="Our Ball World",
                  width = 600, # the width of the canvas
                  height = 600, # the height of the canvas
                  center = vector(0,5,0), # the camera perspective (looking a little down)
                  background = vector(0,.5,.5), # this is an RGB like array
                  resizable = "False") # the canvas cannot be resized.
                  

'''
 create the floor box
'''
L = 10.0
H = 0.2
W = 0.0

my_floor = box(pos=vector(0,-.15,0),
               size = vector(L, H, W),
               color = color.green)

'''
  ball parameters
'''
R = 0.15
start_pos = vector(0,7,0)
ball = sphere(pos = start_pos,radius=R,color=color.red)

# adding loop to create motion of the ball dropping
g = 9.81  #gravitational constant for Earth
t = 0   #start time in seconds
dt = 0.01    #delta time in seconds

velocity = vector(0,0,0)
energy_loss = .85
b = 0.4

while True:
    rate(100)  # Control the simulation speed

    drag_acceleration_y = -b * velocity.y
    total_acceleration_y = -g + drag_acceleration_y
    velocity.y += total_acceleration_y * dt  # Update velocity with gravity
    ball.pos.y += velocity.y * dt  # Update ball position
    # Check for bounce
    if ball.pos.y <= ball.radius :  # When ball hits the floor
      ball.pos.y = ball.radius  # Reset position to the floor level
      velocity.y = -velocity.y * energy_loss  # Reverse velocity and apply energy loss
