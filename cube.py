import os
os.environ['VPYTHON_LAUNCH_BROWSER'] = 'False'

from vpython import *

dx = 2
y = -9
dy = 2
dz = 2


while y < 11:	# Initail loop to set bounds for 'y'; loops until all rows are complete
  x = -9	# Establishing the starting conditions for the nested loop

  while x < 11:		# Sets the bounds for 'x'
    z = 0	# Starting condition for 'z' in next nestes loop

    while z < 21:	# Loop sets that creates the cube
      rate(2)
      box(pos = vec(x,y,z), color = color.green)
      z = z + dz
    x = x + dx
  y = y + dy	# Updates 'y' position for the next row
