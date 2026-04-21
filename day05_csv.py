import pandas as pd

df = pd.read_csv("students.csv")

print(" Full Data:")
print(df)

print("\nFirst 3 rows:")
print(df.head(3))

print("\nInfo:")
print(df.info())

print("\nStatistics:")
print(df.describe())

print("\nAverage Marks:", df["Marks"].mean())

passed = df[df["Marks"] >= 50]
print("\nPassed Students:")
print(passed)

failed = df[df["Marks"] < 50]
print("\nFailed Students:")
print(failed)