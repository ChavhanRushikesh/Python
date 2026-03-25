
#Ass-41
# Write a Python program that classifies a new data point using the K-Nearest Neighbors algorithm. 
# The algorithm should be implemented manually without using any machine learning library.
# The program should:
#   Calculate Euclidean distance
#   Sort distances
#   Select K nearest neighbors
#   Predict the class based on majority voting

#1. Accept X and Y coordinates of a new point from the user.
# 2 Compute Euclidean distance from all dataset points
# 3. Sort the distances.
# 4. Select K=3 nearest neighbors.
# 5. Predict the class label


import math

data = [
    ('A', 2, 3, 'Red'),
    ('B', 3, 3, 'Red'),
    ('C', 3, 1, 'Blue'),
    ('D', 6, 5, 'Blue')
]

x_new = float(input("Enter X coordinate: "))
y_new = float(input("Enter Y coordinate: "))

distances = []
for point in data:
    name, x, y, label = point
    distance = math.sqrt((x - x_new)**2 + (y - y_new)**2)
    distances.append((name, distance, label))

distances.sort(key=lambda x: x[1])

k = 3
neighbors = distances[:k]

votes = {}
for neighbor in neighbors:
    label = neighbor[2]
    votes[label] = votes.get(label, 0) + 1

predicted_class = max(votes, key=votes.get)

print("\nNearest Neighbors:")
for n in neighbors:
    print(f"{n[0]} - Distance: {round(n[1], 2)}")

print("Predicted Class:", predicted_class)