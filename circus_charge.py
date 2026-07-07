import os
os.environ['VPYTHON_LAUNCH_BROWSER'] = 'False'

from vpython import *

scene.height = 600
scene.background = color.white

## the following code creates the grid, arrows representing B, and rings

# Using the funcition 'setup():' from the package vpython
def setup():		# '()' Implies this function only runs once
    grid = []
    xmax = 0.5
    dx = xmax/5
    r = 0.002
    for x in arange(-xmax, xmax+dx, dx):
        grid.append(curve(pos=[vector(x,-xmax,-xmax),vector(x,-xmax,xmax)], color=color.gray(0.4), radius=r))
    for z in arange(-xmax, xmax+dx, dx):
        grid.append(curve(pos=[vector(-xmax,-xmax,z),vector(xmax,-xmax,z)],color=color.gray(0.4), radius=r))
    
    # Creating the magnetic field that effects the particle's motion
    bfield=[]
    bscale = (xmax/3)/mag(B)
    for x in arange(-xmax, xmax+dx, xmax):
        for z in arange(-xmax, xmax+dx, xmax):
            bfield.append(arrow(pos=vector(x,-xmax,z), axis=B*bscale, color=vector(0,0.8,0.8), opacity = 1))   ## opacity 0.5 poor antialiasing
    jhat = vec(0,1,0)  

    rpa = [
        [ vector( 0.338089, 0.0209909, 9.93021e-4 ), vector( -7.58175e-4, 0.0417841, 0.999126 ) ],
        [ vector( -0.30118, 0.083948, -4.86939e-4 ), vector( 1.51241e-3, 0.0831974, -0.996532 ) ],
        [ vector( 0.339271, 0.188871, 1.48176e-3 ), vector( -2.25893e-3, 0.124034, 0.992275 ) ],
        [ vector( -0.302363, 0.33576, -9.77478e-4 ), vector( 2.9942e-3, 0.164102, -0.986439 ) ],
        [ vector( 0.340456, 0.524616, 1.9741e-3 ) , vector( -3.715e-3, 0.203231, 0.979124 ) ],
        [ vector( -0.30355, 0.755437, -1.47164e-3 ),  vector( 4.41851e-3, 0.241271, -0.970448 )]
        ]
        
    for info in rpa:
        ring( pos=info[0], axis=info[1], color=color.magenta, radius = 0.05, thickness = 0.01 )

B = vector(0,.5,0)     # uniform magnetic field
E = vector(0, 1e5, 0)  # uniform electric field

setup()

particle = sphere(pos = vector(-0.3,0,0), radius = 0.0125, make_trail=True, interval=50, color = color.red)
particle.charge = 1.6e-19
particle.mass = 1.7e-27

particle.v = vector(0,0,-1.5e7)					 #initial velocity
attach_arrow(particle, "v", scale=1e-8, color=color.green)

v_label = label(text='Velocity', color=color.red, height=12, box=False, line=False)

particle.Ftot = vec(0, 0, 0)					 # initial force on particle is 0
attach_arrow(particle, "Ftot", scale=1e11, color=color.black)

f_label = label(text='Force', color=color.black, height=12, box=False, line=False)

particle.p = particle.mass * particle.v				 # initial momentum

dt = 2.5e-11
t = 0								 # Start time

k = vec(0, 0, 0)

# Function that resets the test charge back to its starting state
def reset_simulation():
    global t
    t = 0
    particle.pos = vec(-0.3, 0, 0)
    particle.Ftot = vec(0,0,0)
    particle.clear_trail()  # Clears the old line from the screen
    print("Simulation reset!")

# Create the clickable button in the browser canvas
button(text = "Repeat Simulation", bind = reset_simulation)
scene.append_to_caption("\n\n") # Adds vertical spacing below the button

while True:
  rate(1000)
  magnetic_force = cross((particle.v * particle.charge), B) # Takes the cross product of velocity and B-feild vectors multiplied by the particle's charge

  particle.Ftot = magnetic_force + (particle.charge * E)    # Total force on particle 'Lorentz force'
  
  particle.p = particle.p + particle.Ftot * (dt)	    # Particle momentum
  
  particle.v = particle.p/particle.mass			    # Particle velocity
  
  particle.pos = particle.pos + particle.v * (dt)	    # Position update equation
    
  t = t + 1
  t = t + dt
  # Update label positions to float slightly offset from the particle
  v_label.pos = particle.pos + particle.v * 1e-8
  f_label.pos = particle.pos + particle.Ftot * 1e11 + vector(0, 0.03, 0)
