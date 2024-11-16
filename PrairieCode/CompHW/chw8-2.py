import numpy as np
import numpy.linalg as la

transition_matrix = np.array([[-1, -0.18], [0.8, -0.18]])
eigvals, eigvecs = la.eig(transition_matrix)
c = la.solve(eigvecs, np.array([100, 0]))
c1, c2 = c[0], c[1]

# uncomment below to plot g(x) and h(x)
plot_functions(c1, c2, eigvals, eigvecs)
hours = 3