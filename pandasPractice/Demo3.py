#Aceess a group of rows ro columns in a Pandas DataFrame

import pandas as pd
#DataSet

data = {
    'Student':["Jameel","John","Jacob","Hari","Mohan"],
    'Rank':[1,4,3,5,2],
    'Mark':[95,92,80,60,90]
}
df=pd.DataFrame(data,index=['RowA','RowB','RowC','RowD','RowE'])

print("Student Records\n\n",df)

#Access using rows or columns by integer positions

print("\nValue = \n",df.iloc[[3,4]])