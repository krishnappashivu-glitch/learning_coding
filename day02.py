import numpy as np

marks = np.array([98, 56, 45, 87, 76, 86, 95])

average = np.mean(marks)
highest = np.max(marks)
lowest = np.min(marks)

pass_count = np.sum(marks >= 50)
fail_count = np.sum(marks < 50)

print(" NumPy Student Analysis")
print(" ")
print("Marks:", marks)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("Passed:", pass_count)
print("Failed:", fail_count)
