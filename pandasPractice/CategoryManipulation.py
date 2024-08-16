# Append new categories in Pandas
import pandas as pd

# Create a categorical series
s = pd.Series(["p","q","r","s","q"],dtype="category")
print("\n Series:\n",s)

# Append a category
s=s.cat.add_categories("t")

print("\n Updated Categories(Append)\n: ",s)


# Remove a category
s = s.cat.remove_categories("r")
print("\nUpdated Category(Remove)\n:",s)