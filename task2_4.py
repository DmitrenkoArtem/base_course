n=int(input())
for i in range(1,len(str(n))):
    print(n-n%10**i)