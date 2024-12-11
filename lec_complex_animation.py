import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def circle_move(r,vx0,vy0,time):
    x0=vx0*time
    y0=vy0*time
    alpha=np.arange(0,2*np.pi,0.1)
    x=x0+r*np.cos(alpha)
    y=y0+r*np.sin(alpha)
    return x,y

fig,ax=plt.subplots()
ball,=plt.plot([],[],'o',color='r',label='ball')
frames=180
def animation(i):
    ball.set_data(circle_move(r=0.5,vx0=0.01,vy0=0.01,time=i))
    return ball
edge=3
plt.axis('equal')
ax.set_xlim(-edge,edge)
ax.set_ylim(-edge,edge)
anim=FuncAnimation(fig,animation,frames=frames,interval=30)
anim.save('animation.gif',writer='pillow')
