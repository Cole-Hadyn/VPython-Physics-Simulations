
import os
os.environ['VPYTHON_LAUNCH_BROWSER'] = 'False'

from vpython import *

scene.background = color.white
scene.range=0.2  ## this is needed to work around a bug in GlowScript

oofpez = 9e9  # one over four pi epsilon zero
sf = 1e-4 # scale factor for arrows

	# Creating the dipole of particles: (+) charge 1, (-) charge 2
charge_1 = sphere(pos = vec( 1e-2, 0, 0), radius = 5e-3, color = color.red, q = 3e-9)
charge_2 = sphere(pos = vec(-1e-2, 0, 0), radius = 5e-3, color = color.blue, q = -3e-9)

# One observation location to calculate the a baseline E-field once
ob1 = sphere(pos = vec(0.0707, 0.0707, 0), radius = charge_1.radius, color = color.orange, visible = False, E = vec(0,0,0) )


r1 = ob1.pos- charge_1.pos
r2 = ob1.pos- charge_2.pos


# Calculating the E-field applied to the observation point from each particle of the dipole
ob1.E1 = (oofpez * charge_1.q / mag(r1)**2 * hat(r1) )	# E-field of a point charge felt by the observation point
print("ob1.E1 = ", ob1.E1)
ob1.E2 = (oofpez * charge_2.q / mag(r2)**2) * hat(r2)
print("ob1.E2 = ", ob1.E2)

Enet1 = ob1.E1+ob1.E2		   # Net baseline E-field of the dipole
print("Enet1 = ", Enet1)

ob1.E = Enet1
attach_arrow(ob1, "E", scale = sf)   # Displaying E-field applied to observation point

# Loop to display E-field around the dipole with arrows
R = 0.1
theta = 0
dtheta = pi/6
while theta < 2*pi:
    ob = sphere(pos = vec(R*cos(theta), R*sin(theta), 0), radius = charge_1.radius, 
         color = color.orange, E = vec(0,0,0), visible = False)
    attach_arrow(ob, "E", scale = sf)
    r1 = ob.pos- charge_1.pos		# Creates new r1 and r2
    r2 = ob.pos- charge_2.pos
    ob.E1 = (oofpez * charge_1.q / mag(r1)**2) * hat(r1)
    ob.E2 = (oofpez * charge_2.q / mag(r2)**2) * hat(r2)
    Enet = ob.E1+ob.E2
    ob.E = Enet
    attach_arrow(ob, "E", scale=sf)
    print("Enet = ", Enet)

    theta = theta + dtheta

# Creating a charged particle that will navigate the E-field of the dipole
test_charge = sphere(pos = vec(0, R, 0), radius = charge_1.radius, color = color.blue, q = -3e-9, make_trail = True)
test_charge.m = 1e-5
test_charge.p = vec(0, 0, 0)

t = 0
dt = .1
k = vec(0, 0, 0)

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

# Navigating the charge around the E-field
while t < 300:
  rate(120)
  r3 = test_charge.pos - charge_1.pos		# Distance of (+) charge from test charge
  r4 = test_charge.pos - charge_2.pos		# Distance of (-) charge from test charge
  test_charge.E1 = (oofpez * charge_1.q / mag(r3)**2) * hat(r3)	 # Calculating external E-field from each pt. in dipole
  test_charge.E2 = (oofpez * charge_2.q / mag(r4)**2) * hat(r4)
  Enet2 = (test_charge.E1 + test_charge.E2)
  F = test_charge.q * (Enet2)		# Force applied to a point charge from an external E-field
  p = test_charge.p + (F * dt)		# Momentum update eqn.
  test_charge.pos = test_charge.pos + ((p/test_charge.m)*dt)	# Position update eqn.
  t = t + dt

