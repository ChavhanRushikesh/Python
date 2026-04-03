#Ass - 48
#Program - 03

#Write a Python program using StandardScaler to perform feature scaling on the following dataset:
# [[25,20000],
# [30,40000], [35,80000]]
# Print the scaled dataset.

import numpy as np
from sklearn.preprocessing import StandardScaler

data = np.array([[25, 20000], [30, 40000], [35, 80000]])

scaler = StandardScaler()

scaled_data = scaler.fit_transform(data)

print("The scaled dataset is:\n", scaled_data)
