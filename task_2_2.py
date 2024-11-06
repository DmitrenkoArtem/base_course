import numpy as np

a=np.zeros((1,3))

for i in range(3):
    a[0,i]=int(input(f'{i}: '))
print(a)
new=int(input('Число: '))
pos=int(input('Позиция: '))
for i in a[pos:]:
    print(i)