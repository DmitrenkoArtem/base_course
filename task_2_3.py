import matplotlib.pyplot as plt
import numpy as np

def func(a,b):
    x=np.arange(a-10,b+10,1)
    y=np.array()
    for i in x:
        if i<a:
            y.append(a**2)
        elif a<=x<=b:
            y.append(x**2)
        else:
            y.append(b**2)
    plt.plot(x,y)
    plt.axis('equal')
    plt.savefig('task_2_3.png')
if __name__=='__main__':
    func(0,2)