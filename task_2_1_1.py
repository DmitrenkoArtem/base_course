import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig,axis=plt.subplots()
axis.set_xlim(-10,10)
axis.set_ylim(-10,10)
plt.axis('equal')

r=10
alpha=np.linspace(0,10,100)    
x=r*(alpha-np.sin(alpha))
y=r*(1-np.cos(alpha))

frames=len(x)

plot,=axis.plot(x,y)
point,=axis.plot([],[],'o')

def update_point(t):
    point_x=x[t-1:t]
    point_y=y[t-1:t]
    point.set_data(point_x,point_y)
    return point,
animation=FuncAnimation(fig=fig,func=update_point,frames=frames,interval=100)
animation.save('task_2_1_1.gif',writer='pillow')