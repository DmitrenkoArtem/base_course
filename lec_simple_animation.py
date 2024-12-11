import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def circle_move(R,angle_vel,time):
    alpha=angle_vel*np.pi/180*time
    x=R*np.cos(alpha)
    y=R*np.sin(alpha)
    return x,y
fig,ax=plt.subplots()
ball,=plt.plot([],[],'o',color='r',label='ball')
ball_line,=plt.plot([],[],'-',color='r',label='ball')
frames=180
coords=np.zeros((frames,2))
def animation(i):
    coords[i]=circle_move(2,1,i)
    ball.set_data(coords[:i,0],coords[:i,1])
    ball_line.set_data(coords[:i,0],coords[:i,1])
    return ball,ball_line

edge=3
plt.axis('equal')
ax.set_xlim(-edge,edge)
ax.set_ylim(-edge,edge)
anim=FuncAnimation(fig,animation,frames=frames,interval=30)
anim.save('animation.gif',writer='pillow')
