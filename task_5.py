n='Dmitrenko Artem'
u=[ord(i.upper()) for i in n]
l=[ord(i.lower()) for i in n]
print(sum(u+l))