
import os
os.environ['VPYTHON_LAUNCH_BROWSER'] = 'False'

from vpython import *

scene.background = color.white
# the following two lines draw axes
xaxis = curve(pos=[vec(-0.9, 0, 0), vec(0.9, 0, 0)], color=color.gray(0.5))
yaxis = curve(pos=[vec(0,0-0.3, 0), vec(0, 0.3, 0)], color=color.gray(0.5))

L = 1.5  # length of rod

a = cylinder(pos=vec(-L/2, 0, 0), axis=vec(L,0,0), radius=0.04, opacity=0.3)

N = 20 # number of pieces:
dx = L/N  # length of one piece

Q = 3*10**-8   #total charge of the rod
dq = 3*10**-8/N # segment of charge on rod

x = -L/2 + dx/2
while x < 0.95*L/2:
    rate(100)
    sphere(pos=vec(x,0,0), radius=0.02, color=color.red)
    x = x + dx

oofpez = 9e9
sf = 1.2e-4  # Scale factor for the arrows so they fit nicely on screen


# Loop to display E-field around the ROD with arrows
R = 0.25     # Radius of the observation ring around the center of the rod
theta = 0
dtheta = pi/6

while theta < 2*pi:
    # 1. Position the invisible placeholder sphere in a circle
    obs_pos = vec(R*cos(theta), R*sin(theta), 0)
    ob = sphere(pos=obs_pos, radius=0.01, visible=False, E=vec(0,0,0))

    # 2. Reset the field accumulator for THIS specific ring position
    Enet = vec(0,0,0)

    # 3. NESTED LOOP: Integrate over every segment of the rod for this angle
    x_seg = -L/2 + (dx/2)

    while x_seg < L/2:
        segmentpos = vec(x_seg, 0, 0)
        r_vector = ob.pos - segmentpos

        # Calculate dE from this individual segment
        deltaE = oofpez * (dq / mag(r_vector)**2) * hat(r_vector)
        Enet = Enet + deltaE

        x_seg = x_seg + dx

    # 4. Assign the total calculated field to the object and draw the arrow
    ob.E = Enet
    attach_arrow(ob, "E", scale=sf, color=color.orange)
    print(f"Angle {degrees(theta):.0f}°: Enet = {Enet}")

    theta = theta + dtheta

theta = 0
dtheta = pi/6

while theta < 2 * pi:
    # Projection over y-z planes so it forms a ring circling *around* the rod
    obs_pos = vec(x_center, R * cos(theta), R * sin(theta))
    Enet = vec(0,0,0)

    # Calculate total E-field contribution from all N pieces for this angle coordinate
    x_seg = -L/2 + (dx/2)
    while x_seg < L/2:
        segmentpos = vec(x_seg, 0, 0)
        r_vector = obs_pos - segmentpos

        deltaE = oofpez * (dq / mag(r_vector)**2) * hat(r_vector)
        Enet = Enet + deltaE

        x_seg = x_seg + dx

    # Draw the standalone arrow object directly pointing outwards in space
    arrow(pos=obs_pos, axis=Enet * sf, color=color.orange, shaftwidth=0.012)

    theta = theta + dtheta

print("Vector mapping complete.")



obs = sphere(pos=vec(0, 0.1, 0), radius=0.02, color=color.orange, visible=False)
obs.E = vec(0,0,0)
attach_arrow(obs,"E", scale=1e-3)


x = -L/2 + (dx/2)
while x < L/2:
   segmentpos = vec(x,0,0)     ## don't make a sphere, just use the position
   r = (obs.pos - segmentpos)    ## add code to calculate r for this segment ##  (note that segmentpos is a vector, not an object)


   deltaE = oofpez*(dq/mag(r)**2)*hat(r)   ## add code to calculate dE, the electric field due to this segment
          ## update the total
   obs.E= obs.E + deltaE       ## add code to update obs.E

   x = x + dx
print("E =" , obs.E)


# If N = 5 , E = (-210.238, 3127.96, 0)

# If N = 20 , E = (621.115, 2659.06, 0)

# If N = 200 , E = (625.336, 2654.55, 0)

# Electric Field increases as more points are added
