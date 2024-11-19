import random
f=['цв1','цв2','цв3']
c=['белый','синий','красный']
random.shuffle(c)
r=dict(zip(f,c))
print(r)