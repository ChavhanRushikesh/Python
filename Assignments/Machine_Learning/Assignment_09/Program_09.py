#Ass - 48
#Program - 09

#Write a Python program using scikit-learn to generate a classification report for the following data:

# actual = [1,1,1,1,0,0,0,0]
# predicted = [1,1,0,1,0,1,0,0]

# Display the complete classification report including precision, recall, F1-score, and support.

from sklearn.metrics import classification_report

actual = [1, 1, 1, 1, 0, 0, 0, 0]
predicted = [1, 1, 0, 1, 0, 1, 0, 0]

report = classification_report(actual, predicted)

print("Classification Report:\n", report)