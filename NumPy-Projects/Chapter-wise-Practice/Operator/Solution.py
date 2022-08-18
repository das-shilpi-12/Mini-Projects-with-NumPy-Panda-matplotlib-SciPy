import numpy as np
a = [23,67,45,68,74,12,90,34,67,98]
print("a = \n",a)
b = np.array(a)
print("b = \n",b)
c = b.sum()
print("c = \n",c)
d = b[:1]>50
print("d= \n",d)
e = b.reshape((2,5))
print("e = \n",e)
f = e[1,3]==67
print("f = \n",f)
g = e [:,1]>50
g.sum()
h = e [g, ]
print("h= \n",h.shape)
mask = (e[:,1]>=50) & (e[:,0]<=30)
mask.sum()
i = e[mask,]
print("i = \n",i)
