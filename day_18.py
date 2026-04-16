import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "sleeping_hours": [8, 7, 7, 6, 6, 5, 5, 4],
    "marks": [30, 40, 50, 60, 70, 75, 85, 90]
}

df = pd.DataFrame(data)

X = df[["study_hours", "sleeping_hours"]]
y = df["marks"]

model = LinearRegression()
model.fit(X, y)

study = float(input("Enter study hours: "))
sleep = float(input("Enter sleeping hours: "))

# Step 4: Prediction (correct format)
input_data = pd.DataFrame(
    [[study, sleep]],
    columns=["study_hours", "sleeping_hours"]
)
prediction = model.predict(input_data)

print(f"\nPredicted Marks: {prediction[0]:.2f}")

if prediction[0] >= 80:
    print("Performance: Excellent")
elif prediction[0] >= 50:
    print("Performance: Average")
else:
    print("Performance: Poor")
