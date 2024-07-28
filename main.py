import random
import numpy as np
from position_pb2 import Data3d


# Constants
AREA_MAX = 100      # Upper limit of x and y in meters
AREA_MIN = 0        # Lower limit of x and y in meters
HEIGHT_MAX = 10     # Upper limit of z in meters
HEIGHT_MIN = 0      # Lower limit of z in meters
MAX_VELOCITY = 7    # Maximum velocity in meters per second
NUM_SENSORS = 10     # Number of sensors is 10
NOISE = 0.3         # 30cm (0.3m)


#Class to represent a 3D position.
class Data3d:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


""" 
Initializes a random position within defined bounds.
Returns: 
    Data3d: An instance of Data3d with random x, y, and z values. 
"""
def init_position():
    x = np.random.uniform(AREA_MIN, AREA_MAX)
    y = np.random.uniform(AREA_MIN, AREA_MAX)
    z = np.random.uniform(HEIGHT_MIN, HEIGHT_MAX)
    return Data3d(x, y, z)


""" 
Updates the position with a random movement within velocity constraints.
Args: 
    data3d (Data3d): The current position.
Returns: 
    Data3d: The new position with updated x, y, and z values. 
"""
def update_position(data3d): 
    new_x = data3d.x + np.random.uniform(-MAX_VELOCITY, MAX_VELOCITY)
    new_y = data3d.y + np.random.uniform(-MAX_VELOCITY, MAX_VELOCITY)
    new_z = data3d.z + np.random.uniform(-MAX_VELOCITY, MAX_VELOCITY)

    return Data3d(new_x, new_y, new_z)


"""
Ensures the range does not exceed the maximum allowed velocity and bounds.
Args:
    old_position (Data3d): The previous position.
    new_position (Data3d): The newly updated position.
Returns:
    Data3d: The new position adjusted for maximum velocity and within bounds.
"""
def check_range(old_position, new_position):
    """Ensures the velocity does not exceed the maximum allowed velocity."""
    distance = np.linalg.norm([new_position.x - old_position.x, new_position.y - old_position.y, new_position.z - old_position.z])

    if distance > MAX_VELOCITY:       
        scale_factor = MAX_VELOCITY / distance
        new_position.x = old_position.x + (new_position.x - old_position.x) * scale_factor
        new_position.y = old_position.y + (new_position.y - old_position.y) * scale_factor
        new_position.z = old_position.z + (new_position.z - old_position.z) * scale_factor

    new_position.x = np.clip(new_position.x, AREA_MIN, AREA_MAX)
    new_position.y = np.clip(new_position.y, AREA_MIN, AREA_MAX)
    new_position.z = np.clip(new_position.z, HEIGHT_MIN, HEIGHT_MAX)

    return new_position

"""
Adds noise to the position.
Args:
    position (Data3d): The position to which noise will be added.
Returns:
    Data3d: The position with added noise.
"""
def add_noise(position):
    position.x += random.uniform(-NOISE, NOISE)
    position.y += random.uniform(-NOISE, NOISE)
    position.z += random.uniform(-NOISE, NOISE)

    return position