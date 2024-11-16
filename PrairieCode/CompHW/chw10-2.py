import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
from matplotlib import cm

U, S, Vt = la.svd(measurement, full_matrices=False)


differences = np.zeros(len(S))
sigmaO = np.diag(S)

#@ returns the matrix product, not the scalar. That is np.dot
for k in range(len(S)):
    Bk = np.dot(np.diag(S[:k+1]), Vt[:k+1, :])
    Ak = np.dot(U[:, :k+1], Bk)
    differences[k] = la.norm(Ak - exact_data)
    
    
num_layers = np.argmin(differences)

Uden = U[:, num_layers+1]
Sden = np.diag(S[:num_layers+1])
Vden = Vt[:num_layers+1, :]
SV = np.dot(Sden, Vden)

denoised_data = np.dot(U[:, :num_layers+1], np.dot(np.diag(S[:num_layers+1]), Vt[:num_layers+1, :]))

# Plot the data
display_plot(measurement)
display_plot(denoised_data)
display_plot(exact_data)

#uncomment to plot differences
plt.figure()
plt.plot(differences, 'r.')