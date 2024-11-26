import matplotlib.pyplot as plt
import numpy as np

def circle_plotter(r=10):
    x=np.arange(-2*r,2*r,0.1)
    y=np.arange(-2*r,2*r,0.1)
    x,y=np.meshgrid(x,y)
    fxy=x**2+y**2-r**2
    plt.contour(x,y,fxy,levels=[0])
    plt.axis('equal')
    plt.savefig('sd.png')
if __name__=='__main__':
    circle_plotter()