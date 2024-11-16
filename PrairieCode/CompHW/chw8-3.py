import numpy as np
import numpy.linalg as la
import scipy.linalg as sla

def spring_state(k, m, s0, t):
    A = np.array([[0, 1],
                 [-k / m, 0]])
    
    expA = sla.expm(A * t)
    state = expA @ s0



    return state
    