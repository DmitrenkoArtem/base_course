import numpy as np

def func(shape:str,*args):
    if shape=='круг':
        s=args[0]*np.pi*2
    elif shape=='прямоугольник':
        s=args[0]*args[1]
    elif shape=='треугольник':
        s=args[0]*args[1]/2
    return s
print(func('треугольник',1,2))