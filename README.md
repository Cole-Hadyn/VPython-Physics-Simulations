# VPython 3D Physics Simulations

A collection of interactive 3D computational physics engines written in Python utilizing the VPython framework.

## Included Simulations:

### 1. Biot-Savart Point Charge Field (`mag_field_of_moving_charge.py`)
Visualizes the magnetic field vector $\vec{B}$ at six symmetric observation points in real time as a subatomic charged particle flies past at $2 \times 10^3 \text{ m/s}$.

### 2. Lorentz Force Drone Trajectory (`circus_charge.py`)
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

