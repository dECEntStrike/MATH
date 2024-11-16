import numpy as np

# Write your code to calculate w below this line
yw = np.array(z - (alpha * u) - (beta * v))
w = yw / gamma