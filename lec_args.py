def func(a,b):
    x=a*b
    return x
#t=func()

def func(a=1,b=0):
    x=a*b
    return x
print(func(0,0))
print(func())
def func(e,f, a=1,b=0, *args,**kwrgs):
    return
def func(*args):
    args[1]-args[2]
print(func(3,4))# => args=(3,4)
def func(**kwrgs):
    x=kwrgs['a']+kwrgs['b']
    return x