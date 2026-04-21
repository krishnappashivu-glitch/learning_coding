

import pandas as pd

data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Marks": [90, 70, 40, 85, 60]
}

df = pd.DataFrame(data)

print("📊 Student Data")
print(df)


average = df["Marks"].mean()
highest = df["Marks"].max()
lowest = df["Marks"].min()

passed = df[df["Marks"] >= 50]
failed = df[df["Marks"] < 50]

print("\nAverage:", average)
print("Highest:", highest)
print("Lowest:", lowest)

print("\nPassed Students:")
print(passed)

print("\nFailed Students:")
print(failed)