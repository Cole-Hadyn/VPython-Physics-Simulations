Disclaimer: File made with AI assistance.
# VPython 3D Physics Simulations

A collection of interactive 3D computational physics engines written in Python utilizing the VPython framework.

## Some Included Simulations:

### 1. Dynamic Package Collection Simulation (`drone_package_catch.py`) 
This Python script utilizes VPython to simulate a real-time physics environment where an autonomous drone dynamically tracks and intercepts a falling package. Incorporating the Momentum Principle, the simulation models complex behaviors including gravitational pull on both objects, steering force scaling, and aerodynamic drag to ensure a smooth, physically accurate interception before the package impacts the ground.

### 2. Biot-Savart Point Charge Field (`mag_field_of_moving_charge.py`)
Visualizes the magnetic field vector $\vec{B}$ at six symmetric observation points in real time as a subatomic charged particle flies past at $2 \times 10^3 \text{ m/s}$.

### 3. Lorentz Force Drone Trajectory (`circus_charge.py`)
Models a particle tracking system subject to uniform orthogonal electric ($\vec{E}$) and magnetic ($\vec{B}$) fields, plotting momentum variations on a dynamic graph canvas.

## HOW TO--Installation & Local Execution

Because these scripts use standard browser loops over local ports, clone the repository and initialize a virtual environment:

```bash
# Create a virtual environment and activate it
python3 -m venv phys_env --without-pip
source phys_env/bin/activate

# Fetch dependencies safely
curl -sS [https://bootstrap.pypa.io/get-pip.py](https://bootstrap.pypa.io/get-pip.py) | python3
pip install vpython "setuptools<70.0.0"

# Run any simulation
python circus_charge.py
