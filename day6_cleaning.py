import pandas as pd

df = pd.read_csv("students_dirty.csv")


print("📊 Original Data:")
print(df)


df["Marks"] = pd.to_numeric(df["Marks"], errors='coerce')
df["Age"] = pd.to_numeric(df["Age"], errors='coerce')


df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["Age"] = df["Age"].fillna(df["Age"].mean())


df = df.drop_duplicates()


print("\n🧹 Cleaned Data:")
print(df)