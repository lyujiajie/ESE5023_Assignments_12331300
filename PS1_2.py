

#Problem2
import numpy as np
M1 = np.random.randint(1,50,size=(5,10))
M2 = np.random.randint(1,50,size=(10,5))
print(M1)
print(M2)
def Matrix_multip(M1,M2):
    a=M1.shape[0]
    b=M1.shape[1]
    c=M2.shape[1]
    M3=np.empty(shape=(a,c))
    for i in range(a):
        for j in range(c):
            for k in range(b):
                M3[i][j]=M3[i][j]+M1[i][k]*M2[k][j]
    return M3
print(Matrix_multip(M1,M2))
