import numpy as np

# def func(a,b):
#     result=np.zeros((2,b-a-1))
#     for i in range(len(result[0,:])):
#         result[0,i]=a+i+1
#         result[1,i]=(a+i+1)**2
#     return result
# print(func(0,10))

def func (a,b):
    x=np.arange(a,b,0.1)
    y=x**2
    return np.array([x,y])
print(func(0,1))