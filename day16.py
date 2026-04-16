import pandas as pd 

data = {
    "sleeping_hours" : [6,7,5,8,6],
    "marks":[80,50,98,87,86]
}
df = pd.DataFrame(data)
print(df)
X = df[["sleeping_hours"]]
Y = df["marks"]


from sklearn.linear_model import LinearRegression

model=LinearRegression()
model.fit(X,Y)

import pandas as pd

model.predict(pd.DataFrame([[7]], columns=["sleeping_hours"]))
pred = model.predict([[7]])
print("predicted marks :",pred)

import matplotlib.pyplot as plt

plt.scatter(X,Y)
plt.plot(X,model.predict(X))
plt.xlabel("sleeping hours")
plt.ylabel("marks")
plt.title("ML model prediction")
plt.show()