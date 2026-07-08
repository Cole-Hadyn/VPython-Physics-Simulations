# Create the Sun at the origin
sun = sphere(pos=vector(0, 0, 0), radius=0.2, color=color.yellow, emissive=True)

# Define parameters for Earth's orbit
orbit_radius = 1  # Distance from the Sun (in arbitrary units)
orbital_speed = 0.01  # Speed of Earth's orbit (angle per frame)
earth_radius = 0.05  # Earth's radius
earth_angle = 0  # Starting angle of the Earth

# Create Earth object
earth = sphere(pos=vector(orbit_radius, 0, 0), radius=earth_radius, color=color.blue, make_trail=True)

# Main animation loop
while True:
    rate(100)  # Refresh the scene 100 times per second (adjust for performance)

    # Update Earth's position based on its angle
    earth_angle += orbital_speed
    x = orbit_radius * cos(earth_angle)
    y = orbit_radius * sin(earth_angle)
    earth.pos = vector(x, y, 0)  # Set the new position of the Earth
