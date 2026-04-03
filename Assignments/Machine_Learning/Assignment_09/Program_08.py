#Ass - 48
#Program - 08

#Write a Python program that calculates TP, TN, FP, FN for the following arrays:

# actual = [1,1,1,1,0,0,0,0]
# predicted = [1,1,0,1,0,1,0,0]
# Display all four values.

actual_values = [1, 1, 1, 1, 0, 0, 0, 0]
predicted_values = [1, 1, 0, 1, 0, 1, 0, 0]

TP = sum(1 for a, p in zip(actual_values, predicted_values) if a == 1 and p == 1)
TN = sum(1 for a, p in zip(actual_values, predicted_values) if a== 0 and p == 0)
FP = sum(1 for a, p in zip(actual_values, predicted_values) if a == 0 and p == 1)
FN = sum(1 for a, p in zip(actual_values, predicted_values) if a == 1 and p == 0)  

print("True Positive :", TP)
print("True Negative :", TN)
print("False Positive :", FP)
print("False Negative :", FN)
