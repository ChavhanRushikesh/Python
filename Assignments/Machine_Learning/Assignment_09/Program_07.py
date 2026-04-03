#Ass - 48
#Program - 06

#Consider the following data:
# Actual Values [1, 1,1, 1, 0,0,0, ό]
# Predicted Values [1, 1,0, 1,0, 1,0, 0]

# Determine the following values:
# True Positive (TP)
# True Negative (TN)
# False Positive (FP)
# False Negative (FN)

actual_values = [1, 1, 1, 1, 0, 0, 0, 0]
predicted_values = [1, 1, 0, 1, 0, 1, 0, 0]

TP = sum(1 for a, p in zip(actual_values, predicted_values) if a == 1 and p == 1)
TN = sum(1 for a, p in zip(actual_values, predicted_values) if a == 0 and p == 0)
FP = sum(1 for a, p in zip(actual_values, predicted_values) if a == 0 and p == 1)
FN = sum(1 for a, p in zip(actual_values, predicted_values) if a == 1 and p == 0)

print("True Positive (TP):", TP)
print("True Negative (TN):", TN)
print("False Positive (FP):", FP)
print("False Negative (FN):", FN)

""" 
pair of actual vs. predicted values one by one:

Index	Actual	Predicted	Result

    1	    1     	1       TP
    2	    1	    1	    TP
    3	    1	    0	    FN
    4	    1	    1	    TP
    5	    0	    0	    TN
    6	    0	    1	    FP
    7	    0	    0	    TN
    8	    0	    0	    TN

Final counts:

True Positive (TP) = 3
True Negative (TN) = 3
False Positive (FP) = 1
False Negative (FN) = 1

"""