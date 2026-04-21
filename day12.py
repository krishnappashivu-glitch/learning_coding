import pandas as pd
import numpy as np

# Step 1: Create dataset
data = {
    "name": ["A", "B", "C", "D", "E"],
    "marks": [90, None, 70, 60, None],
    "branch": ["CS", "IT", "CS", "IT", "CS"]
}

df = pd.DataFrame(data)
print("Original Data:\n", df)

# Step 2: Handle missing values
df["marks"] = df["marks"].fillna(df["marks"].mean())

# Step 3: Vectorization (no loops)
df["marks"] = df["marks"] + 10          # add 10 marks
df["bonus_marks"] = df["marks"] * 1.1   # bonus calculation

# Step 4: Apply + Lambda (custom columns)

# Status
df["status"] = df["marks"].apply(lambda x: "Pass" if x >= 40 else "Fail")

# Grade
df["grade"] = df["marks"].apply(
    lambda x: "A" if x >= 85 else ("B" if x >= 60 else "C")
)

# Performance
df["performance"] = df["marks"].apply(
    lambda x: "Excellent" if x >= 85 else ("Average" if x >= 60 else "Poor")
)

# Step 5: Analysis
print("\nAverage marks per branch:\n", df.groupby("branch")["marks"].mean())

# Step 6: Sorting
top = df.sort_values(by="marks", ascending=False)

# Final Output
print("\nFinal Data:\n", df)
print("\nTop Students:\n", top)