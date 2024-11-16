import numpy as np
import scipy.linalg as sla

#Step 0: Modify the vector E by appending a zero, so that it looks like the vector E~ above.
e = np.zeros(N+1)
for i in range(0, E.size):
    e[i] = E[i]
e[-1] = 0
#Step 1: Create the matrix A.
coeffs = np.zeros((N+1, N+1))
for i in range(0, R.size):
    coeffs[i, i] = R[i]


A = np.identity(N+1) @ coeffs

A[0:16, 16] = 1
A[16, 0:16] = 1
print(A)

#Step 2: Solve the system AI = E.
#LU decomposition

#Get the lower and upper triangles
p, l, u = sla.lu(A)
#we have that AI = PLU I = E
lSolved = sla.solve_triangular(l, e, lower=True)
I = sla.solve_triangular(u, lSolved)
