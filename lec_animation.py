import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig,ax=plt.subplots()

anim_object,=plt.plot([],[],'-',lw=2)
x,y=[],[]
param=np.linspace(0,2*np.pi,100)
ax.set_xlim(0,2*np.pi)
ax.set_ylim(-1,1)
def update(t):
    x.append(t)
    y.append(np.sin(t))
    anim_object.set_data(x,y)
    return anim_object
anim=FuncAnimation(fig,update,frames=param,interval=50)
anim.save('sd.gif',writer='pillow')