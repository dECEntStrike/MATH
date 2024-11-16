def A_subset(A,n):
    # write some code here
    sum = 0
    i=0
    for i in range(len(A)):
        sum += A[i];
    Asub = A[0:n]
    return (sum, Asub)