import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

data = {
    "sleeping_hours": [6, 7, 5, 8, 6],
    "marks": [80, 50, 98, 87, 86]
}
df = pd.DataFrame(data)  
print(df)

X = df[["sleeping_hours"]]
y = df["marks"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("MAE:", mae)
print("R2 Score:", r2)

results = pd.DataFrame({
    "Actual": y_test,
    "Predicted": y_pred
})

print("\nComparison:\n", results)