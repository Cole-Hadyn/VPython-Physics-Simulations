
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
# =======================================================================
# UNIFIED LOOP: Displays both the X-Y and Y-Z E-field rings around the rod
# =======================================================================
R = 0.25         # Radius of both observation rings
x_center = 0.0   # Center position of the Y-Z ring along the rod
theta = 0
dtheta = pi/6    # 12 symmetric steps around a circle

print("Generating combined vector rings...")

while theta < 2 * pi:
    # ----------------===================================================
    # RING 1: X-Y Plane Ring (Flat circle extending out from the sides)
    # ----------------===================================================
    obs_pos1 = vec(R * cos(theta), R * sin(theta), 0)
    Enet1 = vec(0,0,0)

    # ----------------===================================================
    # RING 2: Y-Z Plane Ring (Vertical collar wrapping around the cylinder)
    # ----------------===================================================
    obs_pos2 = vec(x_center, R * cos(theta), R * sin(theta))
    Enet2 = vec(0,0,0)

    # ----------------===================================================
    # INTEGRATION: Calculate segment contributions for BOTH rings at once
    # ----------------===================================================
    x_seg = -L/2 + (dx/2)
    while x_seg < L/2:
        segmentpos = vec(x_seg, 0, 0)
        
        # Math for Ring 1
        r_vector1 = obs_pos1 - segmentpos
        deltaE1 = oofpez * (dq / mag(r_vector1)**2) * hat(r_vector1)
        Enet1 = Enet1 + deltaE1

        # Math for Ring 2
        r_vector2 = obs_pos2 - segmentpos
        deltaE2 = oofpez * (dq / mag(r_vector2)**2) * hat(r_vector2)
        Enet2 = Enet2 + deltaE2

        x_seg = x_seg + dx

    # ----------------===================================================
    # RENDER: Draw the distinct field arrows for both geometries
    # ----------------===================================================
    # Draw Ring 1 arrow (Cyan so you can tell them apart visually!)
    arrow(pos=obs_pos1, axis=Enet1 * sf, color=color.cyan, shaftwidth=0.012)
    
    # Draw Ring 2 arrow (Orange)
    arrow(pos=obs_pos2, axis=Enet2 * sf, color=color.orange, shaftwidth=0.012)
    
    # Console tracking output
    print(f"Angle {degrees(theta):.0f}° | Ring 1 Enet={Enet1} | Ring 2 Enet={Enet2}")

    theta = theta + dtheta

print("Unified vector mapping complete.")

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
