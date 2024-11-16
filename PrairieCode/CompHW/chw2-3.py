
def investment(p1,p2,p3,assets,t):

  # write your code here
    
    value = p1[t] * assets[0] + p2[t] * assets[1] + p3[t] * assets[2]
    return value