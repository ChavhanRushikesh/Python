#3. Use KNN to predict whether a student passes or fails based on study hours and attendance.

#1. Accept input from user:
#     Study hours
#     Attendance percentage
# 2. Apply KNN algorithm
# 3. Predict whether the student Passes or Fails


import math

data = [
    (2, 60, 'Fail'),
    (5, 80, 'Pass'),
    (6, 85, 'Pass'),
    (1, 50, 'Fail')
]

study = float(input("Enter Study Hours: "))
attendance = float(input("Enter Attendance: "))

distances = []
for sh, att, result in data:
    d = math.sqrt((sh - study)**2 + (att - attendance)**2)
    distances.append((d, result))

distances.sort()

k = 3
count = {}

for i in range(k):
    label = distances[i][1]
    count[label] = count.get(label, 0) + 1

prediction = max(count, key=count.get)

print("Predicted Result:", prediction)