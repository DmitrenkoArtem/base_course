import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig,axis=plt.subplots()
axis.set_xlim([-10,10])
axis.set_ylim([-10,10])
plt.axis('equal')
a=1 #параметр увеличения
frames=10 #количество кадров
alpha=np.linspace(0,2*np.pi,100) #массив значений alpha, для отрисовки круга на каждом кадре

circle,=axis.plot([],[]) #график круга

def update_circle(t):
    r=t*a #радиус
    x=r*np.cos(alpha)
    y=r*np.sin(alpha)
    circle.set_data(x,y) #передача вычисленных координат
    return circle,

animation=FuncAnimation(fig=fig,func=update_circle,frames=frames,interval=50)
animation.save('task_1_2.gif',writer='pillow')