# Concatenate two Pandas DataFrame


import pandas as pd

# Dataset
data1={
    'Id':["s01","s02","s03","s04","s05"],
    'Student':["Jameel","John","Jacob","David","Mohan"],
    'Roll':[101,102,103,104,105]
}

data2={
    'Id': ["s06", "s07", "s08"],
    'Student': ["Ben","Oliver", "Rohit"],
    'Roll': [106,107,108]
}

# DataFrame
dataFrame1=pd.DataFrame(data1, index=["s1","s2","s3","s4","s5"])
print("DataFrame1 =\n",dataFrame1)

dataFrame2=pd.DataFrame(data2,index=["s6","s7","s8"])
print("DataFrame2 =\n",dataFrame2)

# Concatenate two DataFrame
resDF = pd.concat([dataFrame1,dataFrame2])
print("\n concatenating DataFrames=\n",resDF)