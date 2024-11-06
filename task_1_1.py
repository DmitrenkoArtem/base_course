import numpy as np

def func(arr:np.ndarray=np.array([1,2,3])):
    summ=0
    for i in arr[:]:
        summ+=i
    return summ/len(arr)
print(func())