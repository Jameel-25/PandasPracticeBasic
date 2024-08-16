# To iterate a DataFrame and display the column names, use the for loop as in the below example.
import pandas as pd

#Dataset
data = {
    'Student':["Jameel","John","Jacob","Hari","Mohan"],
    'Rank':[1,4,3,5,2],
    'Mark':[95,92,80,60,90]
}

# Use the index argument to set your indexes
df= pd.DataFrame(data,index=['Student1','Student2','Student3','Student4','Student5'])

print("Student Records\n\n",df)

# Iterating
print("\nDisplay the columns:")
for col in df:
    print(col)