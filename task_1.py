import numpy as np
import random
n=10
results=np.array([[random.randint(0,100) for i in range(n)] for i in range(3)])
print(results)
print(results.max(),results.sum())