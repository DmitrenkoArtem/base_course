import matplotlib.pyplot as plt
import numpy as np

def cycloida(r):
    p=np.arange(0,20,0.1)    
    x=r*(p-np.sin(p))
    y=r*(1-np.cos(p))
    plt.plot(x,y,ls='-',lw=1)
    plt.axis('equal')
    plt.savefig('task_1_1_1.png')
def astroida(r):
    p=np.arange(0,20,0.1)
    x=r*np.cos(p)**3
    y=r*np.sin(p)**3
    plt.plot(x,y,ls='-',lw=1)
    plt.axis('equal')
    plt.savefig('task_1_1_2.png')
if __name__=='__main__':
    cycloida(10)
    astroida(10)