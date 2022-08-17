import numpy as np 
a = ["shilpi","das","teahyung","bts"]
print(a)
b = np.array(a) #converting to numpy array
print(b)
print(b.shape) #shape of array
print(b.size) #size of arrray
print(b.dtype) #getting datatype of numpy array
c = b.reshape((2,2)) #reshaping numpy 1D array into 2D array
print(c) 
