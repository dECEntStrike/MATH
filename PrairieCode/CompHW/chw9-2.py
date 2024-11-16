import numpy as np
import numpy.linalg as la
import scipy.linalg as sla
import matplotlib.pyplot as plt

r = np.array(observation_data[0])
o = np.array(observation_data[1]) #the thetas
c = np.cos(o)

A = np.array([c**0, c])
for i in range(0, len(A[1])):
    A[1][i] *= r[i]
#r = beta @ A
A = A.T

# print(r)
# print(c)
# print(A)

left = A.T @ A
right = A.T @ r
B = la.solve(left, right)
print(B)

beta = B[0]
e = B[1]
distance = beta / (1 - e * np.cos(3.81))

# Uncomment to plot estimated orbit
display_regression(beta,e)