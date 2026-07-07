import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

g = 9.81          		# Gravity (m/s^2)
c = 0.1           		# Drag coefficient (kg/m)
m = 1.0           		# Mass of projectile (kg)

v0 = 30.0			# Initial velocity (m/s)
angle = 45.0			# Launch angle in degrees

dt = 0.01			# Time step (seconds)

theta = np.radians(angle)	# Convert angle to radians

# splitting initial velocity into components
x, y = [0.0], [0.0]	  # Initial positions
vx = v0 * np.cos(theta)   # splitting initial velocity into components using cos(theta) = vx / v0
vy = v0 * np.sin(theta)   # sin(theta) = vy / v0

# NUMERICAL INTEGRATION (EULER'S METHOD)
while y[-1] >= 0:  			# Runs until the last element in 'y' equals 0

    v = np.sqrt(vx**2 + vy**2)		# Current speed
    
    fx_drag = -c * v * vx		# Calculate Drag forces: F_drag = c * v^2
    fy_drag = -c * v * vy
    
    # Accelerations: a = F/m (including gravity for y-axis)
    ax = fx_drag / m			# Air drag is the only for effecting horizontal motion
    ay = (-g + fy_drag) / m		# Force of gravity and air drag effect the vertical motion
    
    # Update velocities
    vx += ax * dt
    vy += ay * dt
    
    # Update positions and append to our tracking lists (Euler intergration)
    x.append(x[-1] + vx * dt)
    y.append(y[-1] + vy * dt)

# ANIMATION SETUP
fig, ax_plot = plt.subplots(figsize=(8, 5))	# Figure named ax_plot with given dimensions
ax_plot.set_xlim(0, max(x) * 1.1)		# Provides space b/tw edge of graph and plotted data
ax_plot.set_ylim(0, max(y) * 1.1)
ax_plot.set_xlabel('Distance (meters)')
ax_plot.set_ylabel('Height (meters)')
ax_plot.set_title('Projectile Motion with Air Resistance')
ax_plot.grid(True)

line, = ax_plot.plot([], [], 'r-', lw=2)     # Creates red, solid line of width = 2 starting with empty lists
point, = ax_plot.plot([], [], 'bo', ms=8)    # Creates blue dot with marker size = 8 starting with empty lists

# Using a function from a package to define a function; 'Init' is only run once as the inital function
def init():
    line.set_data([], [])
    point.set_data([], [])
    return line, point

# 'update' runs 'frame' # of times; frame = frame index (e.g. 0, 1, 2, ...)
def update(frame):
    line.set_data(x[:frame], y[:frame])		# Update line data from 0 to current frame index
    point.set_data([x[frame]], [y[frame]])	# Position the moving dot at the current frame index
    return line, point			        	# Data used to plot

# Create animation called 'ani'; Let it be a figure using the data from 'update' to draw the line and point
# Have the # of frames equal len(x) with the initial function be 'init', and have performance boost = true for the rest of the data from 'update'
# Only draw the animation once with time intervals b/tw each frame be 10 mili-seconds

ani = animation.FuncAnimation(fig, update, frames=len(x), init_func=init, blit=True, interval=10, repeat=False)

plt.show()
