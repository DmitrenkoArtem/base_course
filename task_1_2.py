import matplotlib.pyplot as plt
import numpy as np
def hyperbola_plotter(k=1,s=0.1,r=10):
    x1=np.arange(-r,0,s)
    y1=k/x1
    x2=np.arange(0.1,r,s)
    y2=k/x2
    plt.plot(x1,y1)
    plt.plot(x2,y2)
    plt.savefig('task_1_2.png')
if __name__=='__main__':
    hyperbola_plotter(1)