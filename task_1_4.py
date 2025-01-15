import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig,axis=plt.subplots()
axis.set_xlim(-1,1)
axis.set_ylim(-1,1)
axis.axis('equal')
n=20
points,=axis.plot([],[],'o')
x0,y0=0.1,0.1
x=[x0]
y=[y0]
c=0.3
d=0.33
for n in range(1,n):
    x.append((x[n-1])**2-(y[n-1])**2+c)
    y.append(2*x[n-1]*y[n-1]+d)
def update(t):
    points.set_data(x[:t],y[:t])
    return points,
animation=FuncAnimation(fig=fig,func=update,frames=n,interval=100)
animation.save('task_1_4.gif',writer='pillow')