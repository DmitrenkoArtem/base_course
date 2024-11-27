import matplotlib.pyplot as plt
import numpy as np

t=np.arange(0,10,0.1)
bbb=np.pi*2
a=1
aa=1
b=2
bb=2
x=aa*np.sin(a*t+bbb)
y=bb*np.sin(b*t)
plt.plot(x,y)
plt.axis('equal')
plt.savefig('task_2_1.png')