from task_1_1 import g,k,e,h,pi
import numpy as np
h_=100
a_=45
b_=35
v=np.sqrt((g*h_*np.tan(b_)**2) / (2*np.cos(a_)*(1-np.tan(b_)*np.tan(a_))))
t_=200
e_=300
n=(2/np.sqrt(pi))*(h/(k*t_)**(3/2))*e**(-e_/k*t_)*e_**(t_/2)
print(v)
print(n)