#How to compare two numpy Arrays

import numpy as np
a=np.array([1])
b=np.array([4])
c=np.greater(b,a)
d=np.less(a,b)
e=np.minimum(a,b)
print(a==b)
print(c)
print(d)
print(e)

#To  find  the Distinct values or unique values in columns

import pandas as pd
df=pd.read_csv(r"C:\Users\Elangovan\Desktop\Python Learning\Sample.csv")
a=df.nunique()
b=df.memory_usage()
print(a)
print(b)

#matplot library is a statistical purpose,graph

#Numpy Mean

import numpy as np
x=(3,4,5,8,956,83,83)
y=np.mean(x)
print(y)

#Numpy Median

a=(26,36,94)
b=np.median(a)
print(b)

#numpy  mode (to use mode we need to import scipy library)

from scipy import stats 