a=int(input())
b=int(input())
c=int(input())
if a<b+c and b<a+c and c<a+b:
    if a==b==c:
        print('Равносторонний')
    elif a==b or b==c or c==a:
        print('Равнобедренный')
    else:
        print('Разносторонний')
else:
    print('Такого не существует.')