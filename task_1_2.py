import numpy as np

def func(arr:np.ndarray=np.array([1,2,3])):
    prod=1
    for i in arr[:]:
        prod*=i
    return prod
print(func())