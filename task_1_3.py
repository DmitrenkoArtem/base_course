def func(m,h,v):
    g=9.8
    ek=m*v**2/2
    ep=m*g*v
    e=ek+ep
    return e
print(func(1,1,1))