a=int(input())
b=int(input())
if a%b==0:
    print('Делится')
else:
    print(f'Частное - {a//b}, остаток - {a%b}')