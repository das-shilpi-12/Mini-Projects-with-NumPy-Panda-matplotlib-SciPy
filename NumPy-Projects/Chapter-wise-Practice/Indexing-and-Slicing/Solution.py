#indexing $ slicing
import numpy as np 
a = [1,2,3,4,5,6,7,8,9,10]
print("a=\n")
print(a,"\n")
b = np.array(a)
print("b=\n")
print(b,"\n")
#indexing
print("b[1] = ",b[1])
print("b[4] = ",b[4])
print("b[1]+b[3] = " ,b[1]+b[3],"\n")
#slicing
print("b[1:3] = ",b[1:3],"\n")
c = b.reshape((2,5)) # 1D TO 2D ARRAY
print("c = \n")
print(c,"\n")
print("c[1,0:3] = \n",c[1,0:3],"\n")
print("c[:,0:3] = \n",c[:,0:3],"\n")
print("c[1,:] = \n",c[1,:])
