import os
os.environ['VPYTHON_LAUNCH_BROWSER'] = 'False'

from vpython import *

dx = 2
y = -9
dy = 2
dz = 2


while y < 11:	# Initail loop to set bounds for 'y'; loops until all rows are complete
  x = -9	# Establishing the starting conditions for the nested loop

  while x < 11:		# loop creates a row of boxes
    rate(10)
    z = 0
    box(pos = vec(x,y,z), color = color.green)
    x = x + dx

    while z < 21:
      box(pos = vec(x,y,z), color = color.green)
      z = z + dz

  y = y + dy	# Updates 'y' position for the next row
