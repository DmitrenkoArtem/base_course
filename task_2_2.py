import matplotlib.pyplot as plt
import numpy as np

def elips(e,p):
    ugol=np.arange(0,2*np.pi,0.1)
    r=p/(1+e*np.cos(ugol))
    x=r*np.cos(ugol)
    y=r*np.sin(ugol)
    plt.plot(x,y)
    plt.axis('equal')
    plt.savefig('task_2_2.png')
if __name__=='__main__':
    elips(0.8,10)