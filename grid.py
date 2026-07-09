


GlowScript 2.9 VPython
dx = 2
y = -9
dy = 2



while y < 11:	# Initail loop to set bounds for 'y'; loops until all rows are complete
  x = -9	# Establishing the starting conditions for the nested loop

  while x < 11:		# loop creates a row of boxes
      rate(10)
      box(pos=vec(x,y,0), color=color.green)
      x = x + dx

  y = y + dy	# Updates 'y' position for the next row
