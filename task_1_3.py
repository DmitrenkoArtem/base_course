import matplotlib.pyplot as plt
import numpy as np
def elips_plotter(a=1,s=0.1,r=10):
    xr=np.arange(-r,r,s)
    yr=np.arange(-r,r,s)
    x,y=np.meshgrid(xr,yr)
    func=y**2+2*x**2
    plt.contour(x,y,func,levels=[a])
    plt.axis('equal')
    plt.savefig('task_1_3.png')
if __name__=='__main__':
    elips_plotter(50)