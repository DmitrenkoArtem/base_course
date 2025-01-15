import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig,axis=plt.subplots()
axis.set_xlim(-20,20)
axis.set_ylim(-20,20)
plt.axis('equal')

frames=10
alpha=np.linspace(0,2*np.pi,100)
heart,=axis.plot([],[])

vx=0.5
vy=0.5

def update_heart(t):
    x=16*np.sin(alpha)**3+t*vx
    y=13*np.cos(alpha)-5*np.cos(2*alpha)-2*np.cos(3*alpha)-np.cos(4*alpha)+t*vy
    heart.set_data(x,y)
    return heart,
animation=FuncAnimation(fig=fig,func=update_heart,frames=frames,interval=50)
animation.save('task_1_3_2.gif',writer='pillow')