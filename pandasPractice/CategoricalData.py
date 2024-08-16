# A categorical variable takes on a limited number of possible values.
# Examples are gender, blood type, country affiliation, rating, etc

# Create Categorical Series in Pandas

import pandas as pd

# Create a Categorical Series
s = pd.Series(["p","q","r","s","q"],dtype="category")

# Display the series
print("Series = \n",s)

# Create Categorical DataFrame in Pandas
df = pd.DataFrame({"Cat1":list("pqrs"),"Cat2":list("pqrp"),"Cat3":list("qrrr")},dtype="category")

# Display the DataFrame
print("DataFrame = \n",df)

# Display the Datatypes
print("\nDatatypes of each column = \n", df.dtypes)