from task_1_4 import trigonometry_array as ta
import numpy as np

# for i in range(ta.shape[0]):
#     tmp=ta[i,0]
#     ta[i,0]=ta[i,1]
#     ta[i,1]=tmp
# print(ta)

n1=int(input('Первый столбец: '))
n2=int(input('Второй столбец: '))
tmp=np.array(ta[:,n1])
ta[:,n1]=ta[:,n2]
ta[:,n2]=tmp
print(ta)