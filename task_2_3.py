import numpy as np

x=int(input('Ширина: '))
y=int(input('Высота: '))+1
a=np.zeros((y,x))

for x_pos in range(x):
    for y_pos in range(y):
        if y_pos==y-1:
            highest=0
            for maybemax in a[:,x_pos]:
                if maybemax>highest:
                    highest=maybemax
            a[y_pos,x_pos]=highest
        else:
            a[y_pos,x_pos]=int(input(f'Значение для {x_pos},{y_pos}: '))
print(a)