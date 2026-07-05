


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
  obs = sphere(pos=vec(0.1, 0.015, 0), radius=0.003, color=color.orange, visible=True, vel=vec(0, 0,0.088))
  dx = L/N        #Change in X
  x = -L/2 + (dx/2)
  dt = 0.01
  
while t < 100:
    rate(30)
    fieldE = vec(0,0,0)
    x = -L/2 + (dx/2)
    while x < L/2:
      segmentpos = vec(x,0,0)     ## don't make a sphere, just use the position
      r = obs.pos - segmentpos
      fieldNewE = 9e9 * (dQ / mag(r)**2) * hat(r)
      fieldE = fieldE + fieldNewE
      x = x + dx
      force = fieldE * sphereQ
      acceleration = force / 0.0001
      obs.vel = obs.vel + (acceleration * dt)
      obs.pos = obs.pos + (obs.vel *dt)
      t = t + dt

