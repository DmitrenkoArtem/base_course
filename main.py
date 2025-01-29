import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


angle=45
v0=10


g=9.8
alpha=np.linspace(0,10,100)

vy0=np.sin(np.deg2rad(angle))*v0
vx0=np.cos(np.deg2rad(angle))*v0

x=vx0*alpha
y=vy0*alpha-(g*alpha**2)/2


fig,axis=plt.subplots()
axis.set_xlim([-10,10])
axis.set_ylim([-10,10])
plt.axis('equal')

plot,=axis.plot([],[])
#point,=axis.plot([],[])


def update(t):
    plot.set_data(x[:t],y[:t])
    #point.set_data(x[t],y[t])
    return plot,#point


animation=FuncAnimation(fig=fig,func=update,frames=len(alpha),interval=50)
animation.save('result.gif',writer='pillow')