import matplotlib.pyplot as plt
import numpy as np

def lestnitsa(n):
    def add(m):
        plt.plot([m,m,m+1],[m,m+1,m+1])
    for i in range(n):
        add(i)
    plt.savefig('task_2_4.png')
if __name__=='__main__':
    lestnitsa(5)