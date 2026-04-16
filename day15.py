import pandas as pd
import matplotlib.pyplot as plt 

data= {
    "name":[ "A","B","C","D","E"],
    "age":[20,40,25,35,26],
    "marks":[80,70,87,85,75],
    "sleeping hours":[6,7,8,5,6]
    }

df=pd.DataFrame(data)
print(df)

print(df.corr(numeric_only=True))

import seaborn as sns 

sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("correlation heatmap")
plt.show()

plt.scatter(df["age"], df["marks"])
plt.xlabel("age")
plt.ylabel("marks")
plt.title("Age vs Marks")
plt.show()
