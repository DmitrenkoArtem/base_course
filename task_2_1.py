import numpy as np

first=np.zeros((4,3))
second=np.zeros((4,3))
third=np.zeros((4,3))
for i in range(4):
    for j in range(3):
        f=input(f'#1 ({i},{j}): ')
        first[i,j]=f
        s=input(f'#2 ({i},{j}): ')
        second[i,j]=s
        if f>s:
            third[i,j]=f
        else:
            third[i,j]=s
print(first)
print(second)
print(third)