import numpy as np 

a = np.array([1,2,3,4,5])

print(a)

print(a+2)

print(a*3)

print(a[a>3])

print(a>3)

marks = np.array([45, 55, 65, 35, 75])

print(marks+5)

print(marks[marks>=50])


import pandas as pd

data = { "name": ["krishna", "rama", "sita"],
        "marks": [40, 50, 60] }
print(data)

df= pd.DataFrame(data)

print(df)

print(df["marks"])

df["result"]= df["marks"]>=50

print(df)
