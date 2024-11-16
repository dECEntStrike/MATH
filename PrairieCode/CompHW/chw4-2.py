import numpy as np

# Write your code to calculate T below this line
# creating matrix A
A = np.array([[4, -1, 0, 0, 0],[-1, 4, -1, -1, 0],[0, -1, 4, 0, -1],[0, -1, 0, 4, -1],[0, 0, -1, -1, 4]])
# creating matrix B
B = np.array([S[0]+S[1]+S[8], S[2], S[7]+S[8], S[3]+S[4], S[5]+S[6]]) 
# getting value of T by solving sytem of linear equation A*T = B using linalg
T = np.linalg.inv(A).dot(B)
# printing the value of T
print(T)