a=range(0,10,2)
print(a)
print(type(a))
print(a[3])

a='Good'
for i in range(10):
    if i<len(a):
        print(f'{a[i]} - Bad')
    else:
        print(f'{i} - Good')