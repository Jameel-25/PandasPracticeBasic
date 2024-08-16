#Series
#Attributes=>hasnans,dtype,ndim,size,name,index,head(),tail(),info()
import numpy as np
#pandas.series.*

import pandas as pd

# Data

data = [10,20,40,80,100]

# Create a Series using the Series() method
s=pd.Series(data)

# Display the series
print("Series:\n",s)

# Datatype
print("\nSeries Datatype:",s.dtype)

# ndim
print("\nSeries n dimensional:",s.ndim)

# size : Return number of elements
print("\nSeries Elements:",s.size)

# name : Return the name of the attribute
s1=pd.Series(data,name="MyNumberSeries")
print("\n Series name:",s1.name)

#hasnans attribute returns Ture if NaNs are in the Pandas Series
data2 = [10,20,40,80,100,np.nan]
s2=pd.Series(data2,name="MyNumberSeries2")

#Display the series
print("Series hasnans data1:",s1.hasnans)
print("Series hasnans data2:",s2.hasnans)

data4 = [10,20,40,80,100]

#Create a Series using the Series() method
s4=pd.Series(data4,index=["n1","n2","n3","n4","n5",],name="MySeries")
print("Series:\n",s4)
print("\nSeries Index: ",s4.index)

#head()
print("\nhead():\n\n",s4.head())

#tail()
print("\ntail():\n",s4.tail())

#info()
print("\ninfo():\n\n",s4.info)