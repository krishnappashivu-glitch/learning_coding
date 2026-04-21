import pandas as pd
import numpy as np

data = {
    "Name": ["A","B","C","D","E","F"],
    "Marks": [85, 90, 70, 60, 95, 40],
    "StudyHours": [4, 5, 3, 2, 6, 1],
    "SleepHours": [6, 7, 5, 6, 8, 4]
}

df = pd.DataFrame(data)
print(df)
df["Status"] = df["Marks"].apply(lambda x: "Pass" if x >= 40 else "Fail")

df["Performance"] = df["Marks"].apply(
    lambda x: "Excellent" if x >= 85 else ("Average" if x >= 60 else "Poor")
)
df["NormalizedMarks"] = df["Marks"] / 100
print("\nAverage Marks:", np.mean(df["Marks"]))

print("\nTop Students:\n", df.sort_values(by="Marks", ascending=False).head(3))

print("\nLow Performers:\n", df[df["Marks"] < 50])
df["Score"] = df["StudyHours"] * 10 + df["SleepHours"] * 5