#Ass - 48
#Program - 02

#Write a Python program that calculates the variance and standard deviation of the dataset:
# [6, 7, 8, 9, 10, 11, 12]
# Display both results.

import numpy as np

data = [6, 7, 8, 9, 10, 11, 12]

variance = np.var(data)

std_deviation = np.std(data)

print("The variance of the dataset is:", variance)

print("The standard deviation of the dataset is:", std_deviation)
