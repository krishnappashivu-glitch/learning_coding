import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create dataset
data = {
    "Name": ["A", "B", "C", "D", "E", "F"],
    "Marks": [90, 70, 40, 85, 60, 30],
    "Age": [20, 21, 19, 22, 20, 23]
}

df = pd.DataFrame(data)

print("Original Data:\n", df)

# Step 2: Basic EDA
print("\nInfo:\n")
print(df.info())

print("\nDescribe:\n", df.describe())

print("\nMissing Values:\n", df.isnull().sum())

# Step 3: Analysis

# Top students
top = df.sort_values(by="Marks", ascending=False)
print("\nTop Students:\n", top)

# Average marks
print("\nAverage Marks:", df["Marks"].mean())

# Students below 50
low = df[df["Marks"] < 50]
print("\nLow Scoring Students:\n", low)

# Step 4: Add Columns

# Pass/Fail
df["Status"] = df["Marks"].apply(lambda x: "Pass" if x >= 40 else "Fail")

# Grade
df["Grade"] = df["Marks"].apply(
    lambda x: "A" if x >= 85 else ("B" if x >= 70 else ("C" if x >= 50 else "D"))
)

print("\nFinal Data:\n", df)

# Step 5: Visualization

# Bar chart
df.plot(x="Name", y="Marks", kind="bar", title="Marks of Students")
plt.show()

# Histogram
df["Marks"].plot(kind="hist", title="Marks Distribution")
plt.show()