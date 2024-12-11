import matplotlib.pyplot as plt
import numpy as np
def circle_plotter(r=3):
    alpha=np.arange(-2*np.pi,2*np.pi,0.1)
    x=r*np.cos(alpha)
    y=r*np.sin(alpha)
    plt.plot(x,y,ls='--',lw=1)
    plt.axis('equal')
    plt.savefig('sd')
if __name__=='__main__':
    circle_plotter()