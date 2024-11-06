import numpy as np

def fib(n):
    a=np.zeros(n)
    for i in range(len(a)):
        if i==0:
            a[0]=0
        elif i==1:
            a[1]=1
        else:
            a[i]=a[i-1]+a[i-2]
    return a[-1]
print(fib(10))