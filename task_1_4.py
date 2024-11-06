import numpy as np

def func(a,b):
    result=np.zeros((2,b-a-1))
    print(result)
    for i in range(len(result[0,:])):
        result[0,i]=a+i+1
        result[1,i]=(a+i+1)**2
    return result
print(func(0,10))