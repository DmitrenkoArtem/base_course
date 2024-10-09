b1=int(input('Первый член: '))
q=int(input('Знаменатель: '))
length=int(input('Количество членов: '))
for n in range(length):
    print(b1*q**(n))