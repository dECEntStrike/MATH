import numpy as np

# write your code here
a = np.array([[3.0, 1.0],[2.0, 0.0]])
inv = np.array(np.linalg.inv(a))
im = np.array(image)
corrected = inv.dot(im)#dot is matrix mult

# You can use the function "display_image" to display your result
display_image(image)
display_image(corrected)