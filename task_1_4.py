import numpy as np

n=int(input('N: '))
m=int(input('M: '))

trigonometry_array=np.zeros((n, m))

for i in range(n):
    for j in range(m):
        n=np.sin(n*i+m*j+1)
        if n>=0:
            trigonometry_array[i,j]=n
        else:
            trigonometry_array[i,j]=0
print(trigonometry_array)