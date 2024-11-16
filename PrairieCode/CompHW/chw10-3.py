import numpy as np
import numpy.linalg as la

U, S, Vt = la.svd(A)

small_sig = [S[x] for x in range(len(S)) if S[x] <= 0.05]
small_vecs = [Vt[x] for x in range(len(S)) if S[x] <= 0.05]
#loops through each of the vectors and only gets the ones we need for the calculations


related_columns = [[] for sv in range(len(small_vecs))]
# the entries must be lists

# Enter your code here
for s in range(len(small_sig)):
    for v in range(len(small_vecs[s])):
        if abs(small_vecs[s][v]) > 0.1:
            related_columns[s].append(column_names[v])


# This code will print the groups of columns that you have found to be related
for entry in related_columns:
    print(entry)