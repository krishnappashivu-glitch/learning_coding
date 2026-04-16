import pandas as pd

data ={"name":["A","B","C","D","E"],
        "marks":[90,None,70,60,None],
        "branch":["CS","IT","CS","IT","CS"]}

df=pd.DataFrame(data)
print(df)
df["marks"] = df["marks"].fillna(df["marks"].mean())
print(df)

print(df.groupby("branch")["marks"].mean())
top = df.sort_values(by="marks", ascending=False)
print(top)

df["status"] = df["marks"].apply(lambda x: "Pass" if x >= 40 else "Fail")
print(df)

df["performance"] = df["marks"].apply(
    lambda x: "Excellent" if x >= 85 else ("Average" if x >= 60 else "Poor")
)

print(df)