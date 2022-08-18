import numpy as np #importing numpy
n, p = [int(x) for x in input().split()] #taking inputs
a = [] #list
for i in range(n):
    a.append(input().split()) #inserting input in list
b = np.array(a) #creating numpy array
c = b.astype(np.float16) #changing datatype as float
d = c.mean(axis=1) #creating rows mean
e = d.round(2) #rounding off the solution 
print(e) #printing the value
