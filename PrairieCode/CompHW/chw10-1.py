import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

plt.figure()
plt.imshow(altgeld, cmap='gray')

# Compute the SVD and compress the image

U, S, Vt = la.svd(altgeld, full_matrices=False)
# print(U.shape)
# print(S.shape)
# print(Vt.shape)
diag = np.sum(S)
num_layers = 0
qual = 0

while(num_layers < S.size and qual/diag < 0.73):
    qual += S[num_layers ]
    num_layers += 1

num_layers -= 1
print(num_layers)

# Ucomp = U[0:num_layers][0:num_layers]
# Scomp = S[0:num_layers]
# Vtcomp = Vt[0:num_layers][0:num_layers]

altgeld_compressed = np.zeros(altgeld.shape)

for i in range(0, num_layers + 1):
    altgeld_compressed += np.outer(U[:, i], Vt[i]) * S[i]
print(altgeld_compressed)

# Plot the final image

plt.figure()
plt.imshow(altgeld_compressed, cmap='gray')