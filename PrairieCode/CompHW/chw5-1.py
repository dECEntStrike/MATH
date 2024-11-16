import numpy as np
import numpy.linalg as la

#1 layover means a walk of 2
atmost_1_layover = nonstop_flights @ nonstop_flights + nonstop_flights

#to get the number of routes, we ge the value at the indexes of the matrix
num_options = atmost_1_layover[47][66]