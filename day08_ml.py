
df = pd.read_csv("students_dirty.csv")

df["Marks"] = pd.to_numeric(df["Marks"], errors='coerce')
df["Age"] = pd.to_numeric(df["Age"], errors='coerce')

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["Age"] = df["Age"].fillna(df["Age"].mean())

df = df.drop_duplicates()

df["Result"] = (df["Marks"] >= 50).astype(int)

X = df[["Marks", "Age"]]   # Inputs
y = df["Result"]           # Output


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print("Model Accuracy:", accuracy)


new_data = pd.DataFrame([[75, 21]], columns=["Marks", "Age"])
prediction = model.predict(new_data)

print("Prediction (1=Pass, 0=Fail):", prediction[0])