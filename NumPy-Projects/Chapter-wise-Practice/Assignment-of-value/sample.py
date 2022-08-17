#Assigning value
import numpy as np 
a=[9,8,7,6]
print("a = \n",a)
b = np.array(a)
print("b = \n",b)
c=b.reshape(2,2)
print("c = \n",c)
#assigning values
c[0,0]=10
c[1,0]=90
c[1,1]=20
c[0,1] =30
print("c = \n",c)
#Operation
v = np.array([[180, 183], [54, 50]]) 
print("v= \n",v)
print("c+v = \n",c+v)
print(c.shape)
#COMBINING TWO ARRYS
d = c+v
print("d = \n ",d)
e = d.reshape((4,1))
print("e = \n",e)
#hstack || horizontal
f = np.hstack(d)
print("f= \n",f)
#vstack || vertical
g = np.vstack(e)
print("g = \n",e)
#concatenated horizontal
h= np.concatenate((c,v),axis=1)
print("h = \n",h)
#concatenated vartical 
i = np.concatenate((c,v),axis=0)
print("i = \n",i)
