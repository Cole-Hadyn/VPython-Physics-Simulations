import os
os.environ['VPYTHON_LAUNCH_BROWSER'] = 'False'

from vpython import *

# Function to create a yellow arrow at a given position
def create_arrow(position, direction=vector(1, 0, 0), length=2, color=color.yellow):
    my_arrow = arrow(pos=position, axis=direction * length, color=color, shaftwidth=0.05)
    return my_arrow

# A function that draws arrows located on a box whose center is at (0,0)    
def draw_box_o_arrows(boxsize, pos1, pos2, q1, q2, n):
  pi = 3.1416
  for i in range(0,n):
    my_angle = 2.0*pi*i/n
    # Determine the side of the box you are on.
    if my_angle < pi/4:
      position = vector(boxsize,boxsize*tan(my_angle),0)
    elif my_angle < 3.0*pi/4:
      position = vector(boxsize/tan(my_angle),boxsize,0)
    elif my_angle < 5.0*pi/4:
      position = vector(-boxsize,boxsize*tan(my_angle),0)
    elif my_angle < 7.0*pi/4:
      position = vector(boxsize/tan(my_angle),-boxsize,0)
    else:
      position = vector(boxsize,boxsize*tan(my_angle),0)

    E1_pos = position - pos1
    E_mag1 = k*q1/(mag(E1_pos)**2)
    print(E_mag1)

    E2_pos = position-pos2
    E_mag2 = k*q2/(mag(E2_pos)**2)
    print(E_mag2)

    E_total = E_mag1*E1_pos/mag(E1_pos)+E_mag2*E2_pos/mag(E2_pos)

    my_arrow = create_arrow(position, E_total/mag(E_total), 0.35, color.red)



# Set up a background screen
scene2 = canvas(
                title='Vector math for the Electric Field around a point charge',
                width=800, height=600,
                center=vector(0,0,0),
                background=color.cyan
                #resizable=False
                )

# Create a small ball to represent a point charge
pos1 = vector(-2,0,0) # This is the location of the first charge
my_charge = sphere(pos = pos1, radius = 0.05, color =color.blue)

#Add a second point charge
pos2 = vector(2,0,0) # This is the location of the 2nd charge
my_charge2 = sphere(pos = pos2, radius = 0.05, color =color.blue)

# set constants
k = 9.0e9 # Coulombs constant in Nm^2/C^2
q1 = 1.0e-6 # charge 1 in coulombs
q2 = 1.0e-6 # charge 2 in coulombs

n = 20 # number of field points on a box

# This will calculate electric field on a 6x6 box centered on 
# the two charges
boxsize = [0.5, 1.0, 1.5, 2.5, 3.0, 4.0]
for i in range(6):
  print("n = ",n)
  draw_box_o_arrows(boxsize[i], pos1, pos2, q1, q2, n)

# Creating a pt. charge to travel around the electric field of the stationary charges

# Creating a charged particle that will navigate the E-field of the dipole
test_charge = sphere(pos = vec(-1, 0, 0), radius = my_charge.radius, color = color.blue, q = -1.0e-6, make_trail = True)
test_charge.m = 1e-5
test_charge.p = vec(0, 0, 0)



# Navigating the charge around the E-field
while t < 300:
  rate(100)
  r3 = test_charge.pos - my_charge.pos		# Distance of (+) charge from test charge
  r4 = test_charge.pos - my_charge2.pos		# Distance of (-) charge from test charge
  test_charge.E1 = (oofpez * my_charge.q / mag(r3)**2) * hat(r3)	 # Calculating external E-field from each pt. in dipole
  test_charge.E2 = (oofpez * my_charge2.q / mag(r4)**2) * hat(r4)
  Enet2 = (test_charge.E1 + test_charge.E2)
  F = test_charge.q * (Enet2)		# Force applied to a point charge from an external E-field
  p = test_charge.p + (F * dt)		# Momentum update eqn.
  test_charge.pos = test_charge.pos + ((p/test_charge.m)*dt)	# Position update eqn.
  t = t + dt







