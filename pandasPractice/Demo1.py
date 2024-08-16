#Create a Pandas DataFrame
import pandas as pd

#Dataset
data = {
    'Student':["Jameel","John","Jacob","Hari","Mohan"],
    'Rank':[1,2,3,4,5],
    'Mark':[95,92,80,60,90]
}
df=pd.DataFrame(data)

print("Student Records\n\n",df)