import matplotlib.pyplot as plt
import numpy as np

def log_spiral(e,b):
    ugol=np.arange(0,8*np.pi,0.1)
    r=e**(b*ugol)
    x=r*np.cos(ugol)
    y=r*np.sin(ugol)
    plt.plot(x,y)
    plt.axis('equal')
    plt.savefig('task_1_4_log_spiral.png')
def arhimedova_spiral(k):
    ugol=np.arange(0,8*np.pi,0.1)
    r=k*ugol
    x=r*np.cos(ugol)
    y=r*np.sin(ugol)
    plt.plot(x,y)
    plt.axis('equal')
    plt.savefig('task_1_4_arhimedova_spiral.png')
def zhezl(k):
    ugol=np.arange(0.01,8*np.pi,0.1)
    r=k/np.sqrt(ugol)
    x=r*np.cos(ugol)
    y=r*np.sin(ugol)
    plt.plot(x,y)
    plt.axis('equal')
    plt.savefig('task_1_4_zhezl.png')
def roza(k):
    ugol=np.arange(0,8*np.pi,0.1)
    r=np.sin(k*ugol)
    x=r*np.cos(ugol)
    y=r*np.sin(ugol)
    plt.plot(x,y)
    plt.axis('equal')
    plt.savefig('task_1_4_roza.png')
if __name__=='__main__':
    #log_spiral(1.1,2)
    #arhimedova_spiral(10)
    #zhezl(1)
    #roza(2)
    #roza(2.1)