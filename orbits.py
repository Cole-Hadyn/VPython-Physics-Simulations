import os
os.environ['VPYTHON_LAUNCH_BROWSER'] = 'False'

from vpython import *


# Create the Sun at the origin
sun = sphere(pos=vector(0, 0, 0), radius=0.2, color=color.yellow, emissive=True)

R_a = 1.4	# Longest distance from the Sun
R_p = 0.7	# Shortest distance from the Sun

e = (R_a - R_p) / (R_a + R_p)	# eccentricity formula
a = (R_a + R_p) /2 		# Semi-major axis

print(f"Calculated Eccentricity (e) = {e:.3f}")
print(f"Semi-major axis (a) = {a:.3f}")


# Define parameters for Earth's orbit
orbital_speed = 0.02  # Speed of Earth's orbit (angle per frame)
earth_radius = 0.04  # Earth's radius
earth_angle = 0  # Starting angle of the Earth

# Parameter for Moon's orbit
moon_orbit_radius = 0.15	# Orbit radius of the Moon
moon_speed = 0.15			# Moon speed
moon_radius = 0.015		# Radius of the Moon
moon_angle = 0

# Create Earth object
earth = sphere(pos=vector(R_p, 0, 0), radius=earth_radius, color=color.green, make_trail=True)

# Create moon object
moon = sphere(pos=earth.pos + vector(moon_orbit_radius, 0, 0), radius=moon_radius, color=color.gray(0.7), make_trail=False)

# Main animation loop
while True:
    rate(100)  # Refresh the scene 100 times per second (adjust for performance)

    r = (a * (1 - e**2)) / (1 + e * cos(earth_angle))

    # Update Earth's position based on its angle
    x = r * cos(earth_angle)     # Convert polar coordinates (r, theta) into standard 3D Cartesian coordinates (x, y, z)
    y = r * sin(earth_angle)
    earth.pos = vector(x, y, 0)  # Set the new position of the Earth

    x_moon_offset = moon_orbit_radius * cos(moon_angle)
    y_moon_offset = moon_orbit_radius * sin(moon_angle)
    moon.pos = earth.pos + vector(x_moon_offset, y_moon_offset, 0)


    earth_angle += orbital_speed
    moon_angle += moon_speed
