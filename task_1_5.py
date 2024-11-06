import numpy as np

def func(shape:str,*args)
    if shape=='круг':
        s=args[1]*np.pi*2
    elif shape=='прямоугольник':
        s=args[1]*args[2]
    elif shape=='треугольник':
        s=args[1]*args[2]/2
    return s
print(func('треугольник'),)