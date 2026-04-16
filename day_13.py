import pandas as pd

data = {
    "name": ["A", "B", "C", "D", "E"],
    "marks": [85, 90, 70, 60, 95],
    "branch": ["CS", "IT", "CS", "IT", "CS"]
}

df = pd.DataFrame(data)
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.isnull().sum())

import matplotlib.pyplot as plt

df.groupby("branch")["marks"].mean().plot(kind="bar")
plt.title("Average Marks per Branch")
plt.show()

df["marks"].plot(kind="hist")
plt.title("Marks Distribution")
plt.show()
