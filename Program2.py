#Write a Python program that demonstrates how prediction changes when K changes.

# Predict the class of the same new point using:
#   K=1
#   K=3
#   K=5
# Explain why the prediction changes when K increases.






import math

data = [
    ('A', 2, 3, 'Red'),
    ('B', 3, 3, 'Red'),
    ('C', 3, 1, 'Blue'),
    ('D', 6, 5, 'Blue')
]

x = float(input("Enter X coordinate: "))
y = float(input("Enter Y coordinate: "))

distances = []
for name, x1, y1, label in data:
    d = math.sqrt((x1 - x)**2 + (y1 - y)**2)
    distances.append((d, label))

distances.sort()


def predict(k):
    count = {}
    for i in range(k):
        label = distances[i][1]
        count[label] = count.get(label, 0) + 1
    return max(count, key=count.get)

print("\nPrediction Results:")
print("K = 1 →", predict(1))
print("K = 3 →", predict(3))
print("K = 4 →", predict(4))  