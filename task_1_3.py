from task_1_1 import g
import numpy as np

x0=0
y0=0
vx0=1
vy0=2

# results=np.zeros((3,t+1))

# for i in range(t+1):
#     results[0,i]=i
#     x=x0+vx0*i
#     results[1,i]=x
#     y=y0+vy0*i-(g*i**2)/2
#     results[2,i]=y

# print(results)

t = np.arange(0, 1, 0.01)
x = x0 + vx0 * t
y = y0 + vy0 * t - g * t**2 / 2

print(t)
print(x)
print(y)

coords = np.array(tuple(zip(t, x, y)))
print(coords)