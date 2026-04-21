import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Marks": [90, 70, 40, 85, 60]
}

df = pd.DataFrame(data)


plt.figure()
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

plt.figure()
plt.hist(df["Marks"])
plt.title("Marks Distribution")
plt.show()

plt.figure()
sns.barplot(x="Name", y="Marks", data=df)
plt.title("Marks (Seaborn)")
plt.show()