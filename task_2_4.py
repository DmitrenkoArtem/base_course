import matplotlib.pyplot as plt
import numpy as np

def lestnitsa(n):
    def add(h):
        plt.plot([h,h,h+1],[h,h+1,h+1])
    for i in range(n):
        add(i)
    plt.savefig('task_2_4_1.png')
def lestnitsa2(n):
    x=[]
    y=[]
    for i in range(n):
        x.append(i)
        y.append(i)
        x.append(i)
        y.append(i+1)
        x.append(i+1)
        y.append(i+1)
    plt.plot(x,y)
    plt.savefig('task_2_4_2.png')
def lestnitsa3(n):
    x=np.arange(0,n,0.1)
    y=x//1
    plt.plot(x,y)
    plt.savefig('task_2_4_3.png')
if __name__=='__main__':
    #lestnitsa(10)
    #lestnitsa2(10)
    #lestnitsa3(10)