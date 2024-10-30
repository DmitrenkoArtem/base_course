x0=10 #гл. обл. видимости
def move(t): #гл. обл. видимости
    x=x0*t #лок. обл. видимости
    return x #лок. обл. видимости
print(move(3))
#print(x)

a='g'
def myfunc():
    a='b'
    print(a)
myfunc()
print(a)