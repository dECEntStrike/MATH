import numpy as np

# This is your original image
display_image(image)

# modify the definition of the 'sheared' variable to apply the correct transformation
xVals = np.array(image[0])#the first array is x values
yVals = np.array(image[1])

newX = np.array(xVals + (0.7 * yVals))
sheared = np.array([newX, yVals])
display_image(sheared)

# modify the definition of the 'rotated' variable to apply the correct transformation
newX = np.array(xVals * np.cos(np.pi /3) - yVals * np.sin(np.pi /3))
newY = np.array(xVals * np.sin(np.pi /3) + yVals * np.cos(np.pi /3))
rotated = np.array([newX, newY])
display_image(rotated)

# modify the definition of the 'sheared_and_rotated' variable to apply the correct transformation
newX = np.array(xVals + (0.7 * yVals))
bothX = np.array(newX * np.cos(np.pi /3) - yVals * np.sin(np.pi /3))
newY = np.array(newX * np.sin(np.pi /3) + yVals * np.cos(np.pi /3))
sheared_and_rotated = np.array([bothX, newY])
display_image(sheared_and_rotated)