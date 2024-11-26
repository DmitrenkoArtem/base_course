import matplotlib.pyplot as plt
x=[3,8,5]
y=[7,4,9]
plt.plot(x,y,color='g',label='гол',marker='>',ms=5)
plt.plot(y,x,color='r',label='гол 2',marker='o',ms=3)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('графики')
plt.grid()
plt.savefig('графики')