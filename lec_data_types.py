def changer(a,b):
    a=2
    b[0]='Good'
x=10
L=[1,2]

changer(x,L[:])
print(x,L)

changer(x,L)
print(x,L)

x=3
y=4
z=complex(x,y)
w=complex(y,x)
print(z+w)

s='sdad'
print(s[0])
#s[0]='q'

t=(1,4,9)
print(t)
print(t[0])
#t[0]=3

l=[1,4,9]
l[0]=3
print(l)

d={'al':4,'al':4,}
print(d['al'])
d[4]='hi'
print(d)