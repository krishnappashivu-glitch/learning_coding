import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("students_dirty.csv")

df["Marks"] = pd.to_numeric(df["Marks"], errors='coerce')
df["Age"] = pd.to_numeric(df["Age"], errors='coerce')
print("Original Data:")
print(df)

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["Age"] = df["Age"].fillna(df["Age"].mean())

df = df.drop_duplicates()

print("Cleaned Data:")
print(df)

plt.figure()
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks (Cleaned Data)")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

plt.figure()
plt.hist(df["Marks"])
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

pass_count = (df["Marks"] >= 50).sum()
fail_count = (df["Marks"] < 50).sum()

plt.figure()
plt.pie([pass_count, fail_count], labels=["Pass", "Fail"], autopct="%1.1f%%")
plt.title("Pass vs Fail")
plt.show()