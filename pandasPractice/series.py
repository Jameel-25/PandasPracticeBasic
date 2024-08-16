# Series in Pandas is a one-dimensional array, like a column in a table. It is labeled array that can hold data
# of any type. The Series() method is used for this and has the follwoing paremters.
# data,index,dtype,name,copy

import pandas as pd

# Data
data=[10,20,30,40,80,100]

# Create a Series using the Series() method

s=pd.Series(data)

# Display the Series
print("Series:\n",s)

# []
# Access a value
print("Value from a Pandas Series:",s[2])

# index names
s=pd.Series(data, index=["a","b","c","d","e","f"])

#Display the series
print("\n Series (with the custom labels):\n",s)

#Access a value referring the label
print("\nValue from a Pandas Series with label d:\n",s["d"])