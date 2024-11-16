import numpy as np
import numpy.linalg as la
import scipy.linalg as sla
import matplotlib.pyplot as plt

left = np.array([trial_data[0]**0, trial_data[0]])
left = left.T
right = np.array(trial_data[1])
right = left.T @ right
left = left.T @ left

beta = la.solve(left, right)

#y = 23
#y = BA = 23
#23 = B1 + B2 x

dosage = (23 - beta[0]) / beta[1]

# Uncomment to display least squares line
display_regression(beta)