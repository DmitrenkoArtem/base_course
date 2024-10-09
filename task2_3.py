n=int(input())
for i in range(len(str(n))):
    print((n%10**(i+1))//10**i,end='')