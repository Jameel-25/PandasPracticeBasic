import pandas as pd

# Data
data1 = [10, 20, 30, 40, 80, 101]
data2 = [24, 3, 8, 96, 45, 6]

# Create a Series using the Series() method
series1 = pd.Series(data1)
series2 = pd.Series(data2)

print("Series1:\n", series1)
print("Series2:\n", series2)

# Function to return the larger of the two values
def demo(x1, x2):
    return max(x1, x2)

# Combine two series into one
# The function returns the largest value
res = series1.combine(series2, demo)

print("\nAfter Combining\n", res)