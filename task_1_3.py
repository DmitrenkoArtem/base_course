from task_1_1 import g
import numpy as np

x0=float(input('x0: '))
y0=float(input('y0: '))
vx0=float(input('vx0: '))
vy0=float(input('vy0: '))
t=5

results=np.zeros((3,t+1))

for i in range(t+1):
    results[0,i]=i
    x=x0+vx0*i
    results[1,i]=x
    y=y0+vy0*i-(g*i**2)/2
    results[2,i]=y

print(results)