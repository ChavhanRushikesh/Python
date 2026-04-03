#Ass - 48
#Program - 04

#Write a Python program to calculate the Euclidean distance between two points before and after applying feature scaling, 
# and explain the difference in results.

import numpy as np
from sklearn.preprocessing import StandardScaler

point1 = np.array([25, 20000])
point2 = np.array([30, 40000])

euclidean_distance_before = np.linalg.norm(point1 - point2)
print("Euclidean distance before scaling:", euclidean_distance_before)

data = np.array([point1, point2])

scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

euclidean_distance_after = np.linalg.norm(scaled_data[0] - scaled_data[1])
print("Euclidean distance after scaling:", euclidean_distance_after)


# Explanation:
# Before scaling, the Euclidean distance is influenced by the scale of the features. In this case, the second feature 
# (income) has a much larger scale than the first feature (age),which can dominate the distance calculation. After applying 
# feature scaling, both features are on the same scale, and the distance is more balanced, reflecting the true relationship 
# between the points without being skewed by the magnitude of the features.   
