import numpy as np
import numpy.linalg as la

M = A.copy().astype(float)
for i in range(0, A[0].size):
    M[:, i] /= np.sum(A[:, i], 0)
    #print(M)

a = 0.85
G = (a * M) + ((1-a)/(A[0].size)) * np.ones(A[0].size)
x = power_iteration(G, G[:, 0])
protagonist = names[np.argmax(x)]

# uncomment below to print name of the protagonist
print(protagonist)