import numpy as np
import numpy.linalg as la

def connected(network, degree):
    # network is a network (given as an adjacency matrix) and degree is the degree of separation you want to check
    walks = np.identity(network.shape[0])
    for count in range (1, degree+1):
        walks += la.matrix_power(network, count)
        
    return np.all(walks > 0)
    #the spot ij is the NUMBER OF WALKS of length degree from j to i
