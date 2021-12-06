#Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

#Import the numpy package as np
import numpy as np

#Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

#Print out type of no_baseball
print(type(np_baseball))

import numpy as np
#height is available as a regular list
height = [57.09, 64.57, 77.61, 72.05, 79.00, 78.75, 80.70, 74.45]

#Create a numpy array from height_in: np_height_in
np_height_in = np.array(height)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_height_m = np_height_in * 0.0254

# Print np_height_m
print(np_height_m)

