import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv("students_dirty.csv")

df["Marks"] = pd.to_numeric(df["Marks"], errors='coerce')
df["Age"] = pd.to_numeric(df["Age"], errors='coerce')

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["Age"] = df["Age"].fillna(df["Age"].mean())
df = df.drop_duplicates()

df["Result"] = (df["Marks"] >= 50).astype(int)

X = df[["Marks", "Age"]]   # Input features
y = df["Result"]           # Output (Pass/Fail)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
print("Accuracy:", accuracy)
print("\nConfusion Matrix:\n", cm)

import seaborn as sns
import matplotlib.pyplot as plt
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=["Fail", "Pass"],
            yticklabels=["Fail", "Pass"])

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")

plt.show()