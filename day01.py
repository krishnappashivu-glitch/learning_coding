
marks = [85, 72, 90, 66, 58, 40, 77]

average = sum(marks) / len(marks)

highest = max(marks)
lowest = min(marks)

pass_count = 0
fail_count = 0

for mark in marks:
    if mark >= 60:
        pass_count += 1
    else:
        fail_count += 1

print(" Student Performance Analysis")
print("  ")
print("Marks:", marks)
print("Average:", round(average, 2))
print("Highest:", highest)
print("Lowest:", lowest)
print("Passed:", pass_count)
print("Failed:", fail_count)