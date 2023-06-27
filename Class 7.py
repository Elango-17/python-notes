#series into frame

import asyncio
import pandas as pd 
data={
    'name':["elan","kiran","vadak"],
    'age':[21,19,19],
    'city':['chennai',"chennai","North"]
}
df=pd.DataFrame(data)
print(df)

#Series

import pandas as pd 
data={
    'name':["elan","kiran","vadak"],
    'age':[21,19,19]
}
df=pd.Series(data)
print(df)
print(df[1]) #access indexing

#Creating Lables

import pandas as pd 
a=[1,2,3]
b=pd.Series(a,index=["x","y","z"])
print(b) 
print(b["x"]) #returning the values
print(b["z"])


#Dictionary creation

import pandas as pd 
a={"day 1":5,"day 2":17,"day 3":20}
b=pd.Series(a)
print(b)




