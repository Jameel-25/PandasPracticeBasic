# The join() method will join the columns of the two different DataFrames.
import pandas as pd

#Dataset
data1={
    'Id':["s01","s02","s03","s04","s05"],
    'Student':["Jameel","John","Jacob","David","Mohan"],
    'Roll':[101,102,103,104,105]
}

data2={
    'Rank':[1,4,3,5,2],
    'Mark':[95,70,80,60,90]
}

#DataFrame
dataFrame1=pd.DataFrame(data1)
print("DataFrame1 =\n",dataFrame1)

dataFrame2=pd.DataFrame(data2)
print("DataFrame2 =\n",dataFrame2)

# Join two DataFrames
resDF = dataFrame1.join(dataFrame2)
print("\nJoining two DataFrames:\n",resDF)