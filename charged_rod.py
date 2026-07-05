import os
os.environ['VPYTHON_LAUNCH_BROWSER'] = 'False'

from vpython import *

scene.background = color.white
# the following two lines draw axes
xaxis = curve(pos=[vec(-0.9, 0, 0), vec(0.9, 0, 0)], color=color.gray(0.5))
yaxis = curve(pos=[vec(0,0-0.3, 0), vec(0, 0.3, 0)], color=color.gray(0.5))

L = 1.5  # length of rod

a = cylinder(pos=vec(-L/2, 0, 0), axis=vec(L,0,0), radius=0.04, opacity=0.3)

N = 200 # number of pieces:  
dx = L/N  # length of one piece

Q = 3*10**-8   #total charge of the rod
dq = 3*10**-8/N # segment of charge on rod

x = -L/2 + dx/2
while x < 0.95*L/2:
    rate(100)
    sphere(pos=vec(x,0,0), radius=0.02, color=color.red)
    x = x + dx


obs = sphere(pos=vec(0, 0.1, 0), radius=0.02, color=color.orange, visible=False)
obs.E = vec(0,0,0)
attach_arrow(obs,"E", scale=1e-3)

oofpez = 9e9 

x = -L/2 + (dx/2)
while x < L/2:
   segmentpos = vec(x,0,0)     ## don't make a sphere, just use the position
   r = (obs.pos - segmentpos)    ## add code to calculate r for this segment ##  (note that segmentpos is a vector, not an object)
   
   
   deltaE = oofpez*(dq/mag(r)**2)*hat(r)   ## add code to calculate dE, the electric field due to this segment
          ## update the total
   obs.E= obs.E + deltaE       ## add code to update obs.E 
   attach_arrow(obs,"E", scale=1e-3)

   x = x + dx
print("E =" , obs.E)


# If N = 5 , E = (-210.238, 3127.96, 0)

# If N = 20 , E = (621.115, 2659.06, 0)

# If N = 200 , E = (625.336, 2654.55, 0)

# Electric Field increases as more points are added
