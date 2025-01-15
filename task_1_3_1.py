import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig,axis=plt.subplots()
axis.set_xlim(-5,5)
axis.set_ylim(-5,5)
plt.axis('equal')

frames=10
alpha=np.linspace(0,12*np.pi,1000)
butterfly,=axis.plot([],[])

vx=0.1
vy=0.1

def update_butterfly(t):
    x=np.sin(alpha)*(np.e**np.cos(alpha)-2*np.cos(4*alpha)+(np.sin(alpha/12))**5)+t*vx
    y=np.cos(alpha)*(np.e**np.cos(alpha)-2*np.cos(4*alpha)+(np.sin(alpha/12))**5)+t*vy
    butterfly.set_data(x,y)
    return butterfly,
animation=FuncAnimation(fig=fig,func=update_butterfly,frames=frames,interval=50)
animation.save('task_1_3_1.gif',writer='pillow')