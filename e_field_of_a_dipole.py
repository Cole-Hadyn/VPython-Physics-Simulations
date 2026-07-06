scene.background = color.white
scene.range=0.2  ## this is needed to work around a bug in GlowScript

oofpez = 9e9  # one over four pi epsilon zero
sf = 1e-4 # scale factor for arrows

p1 = sphere(pos=vec( 1e-2, 0, 0), radius=5e-3, color=color.red, q = 3e-9)
p2 = sphere(pos=vec(-1e-2, 0, 0), radius=5e-3, color=color.blue, q = -3e-9)

# one observation location
ob1 = sphere(pos=vec(0.0707, 0.0707, 0), radius=p1.radius, color=color.orange, visible = False, E = vec(0,0,0) )


r1= ob1.pos- p1.pos
r2= ob1.pos- p2.pos



ob1.E1= (oofpez * p1.q / mag(r1)**2 * hat(r1) )
print("ob1.E1=", ob1.E1)
ob1.E2= (oofpez*p2.q / mag(r2)**2) * hat(r2)
print("ob1.E2=", ob1.E2)

Enet1= ob1.E1+ob1.E2
print("Enet1=", Enet1)

ob1.E = Enet1
attach_arrow(ob1, "E", scale=sf)


# Loop to give the Different Mag fields
R = 0.1
theta = 0
dtheta = pi/6
while theta < 2*pi:
    ob = sphere(pos=vec(R*cos(theta), R*sin(theta), 0), radius=p1.radius, 
         color=color.orange, E = vec(0,0,0), visible=False)
    attach_arrow(ob, "E", scale=sf)
    r1 = ob.pos- p1.pos
    r2 = ob.pos- p2.pos
    ob.E1= (oofpez*p1.q / mag(r1)**2) * hat(r1)
    ob.E2= (oofpez*p2.q / mag(r2)**2) * hat(r2)
    Enet= ob.E1+ob.E2
    ob.E = Enet
    attach_arrow(ob, "E", scale=sf)
    print("Enet=", Enet)
    
    theta = theta + dtheta

p3 = sphere(pos=vec(0, R, 0), radius=p1.radius, color=color.blue, q=-3e-9, make_trail = True)
p3.m = 1e-5
p3.p = vec(0, 0, 0)

t = 0
dt = .1
while t < 100:
  rate(100)
  r3 = p3.pos - p1.pos
  r4 = p3.pos- p2.pos
  p3.E1= (oofpez*p1.q / mag(r3)**2) * hat(r3)
  p3.E2= (oofpez*p2.q / mag(r4)**2) * hat(r4)
  Enet2 = (p3.E1 + p3.E2)
  F = p3.q * (Enet2)
  v = p3.p + (F * dt)
  p3.pos = p3.pos +((v/p3.m)*dt)
  t = t + dt

