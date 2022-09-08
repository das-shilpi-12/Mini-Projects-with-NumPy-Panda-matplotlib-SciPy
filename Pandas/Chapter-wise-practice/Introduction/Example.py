import pandas as pd 
import numpy as np
A = pd.Series([1,2,3,4],index=['a','b','c','d']) # with index
print (A)
B = pd.Series(np.array([1,2,3,4]),index = ['e','f','g','h']) #WITH 1d ARRAY
print(B)
C = pd.Series({'i':1,'j':2,'k':3}) # from dict
print(C)
print(C['j'])
