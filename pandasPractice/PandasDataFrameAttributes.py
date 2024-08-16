# Attributes and Methods
# The Pandas DataFrame is a Two-Dimensional, tabular data, that uses the DataFrame()
# method to create a DataFrame. It also uses different built-in attributes and methods
# for basic functionalities.

# dtypes
# ndim
# size
# shape
# index
# T
# head()
# tail()

# Pandas DataFrame dtypes attribute

import pandas as pad
import pandas as pd

# Dataset
data ={
    'Student':["Jameel","John","Jacob","David","Steve"],
    'Rank':[1,4,3,5,2],
    'Marks':[95,70,80,60,90]
}

# Create a Database using the DataFrame() method with index
df=pd.DataFrame(data,index=['RowA','RowB','RowC','RowD','RowE'],)

print("Student records:\n",df)

print("\nDatatypes:",df.dtypes)

print("\nData ndim:",df.ndim)

print("\nNumber of elements:",df.size)

print("\n Dimensions:",df.shape)

print("\n DataFrame Index:",df.index)

print("\n Transpose of DataFrame:\n\n",df.T)

print("\n Head method, it will display first five rows by default:\n")
print(df.head())

print("\n Head method, it will display first three rows:\n")
print(df.head(3))

print("\n Tail method, it will display last five rows by default:\n")
print(df.tail())

print("\n Tail method, it will display last two rows:\n")
print(df.tail(2))


