import time
m=3
n=2
timestart=time.time()
for i in range(m):
    time.sleep(1)
    print(i)
    for q in range(n):
        time.sleep(1)
        print(q)
print(time.time()-timestart)