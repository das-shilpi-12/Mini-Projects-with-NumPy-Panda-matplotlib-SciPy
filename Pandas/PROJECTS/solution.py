import numpy as np
r = int(input()) 
lst = [float(x) for x in input().split()]
arr = np.array(lst)
print(arr.reshape(r,-1).round(2))
