# The index argument  is used to set and name your own indexes in a DataFrame.
# Name your indexes in a Pandas DataFrame

import pandas as pd

#DataSet
data = {
    'Student':["Jameel","John","Jacob","Hari","Mohan"],
    'Rank':[1,4,3,5,2],
    'Mark':[95,92,80,60,90]
}

# Use the index argument to set your indexes
df= pd.DataFrame(data,index=['Student1','Student2','Student3','Student4','Student5'])
print("Student Records\n\n",df)