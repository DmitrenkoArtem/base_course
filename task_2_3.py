import matplotlib.pyplot as plt
import numpy as np

def func(a,b):
    x1=np.arange(a-10,a,0.1)
    x2=np.arange(a,b,0.1)
    x3=np.arange(b,b+10,0.1)
    y1=x1/x1*a**2
    y2=x2**2
    y3=x3/x3*b**2
    plt.plot(x1,y1)
    plt.plot(x2,y2)
    plt.plot(x3,y3)
    plt.axis('equal')
    plt.savefig('task_2_3.png')
if __name__=='__main__':
    func(0,2)