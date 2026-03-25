#Train the model using only:
# StudyHours
# Attendance
# Compare the accuracy with the full-feature model. Is the model still performing well?

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# --------------------------------------------------
# Function 1 : Train model with ALL features
# --------------------------------------------------
def fullModel(dataPath):

    df = pd.read_csv(dataPath)

    X = df[['StudyHours','Attendance','PreviousScore','AssignmentsCompleted','SleepHours']]
    Y = df['FinalResult']

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier()

    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    return accuracy_score(Y_test, Y_pred)


# --------------------------------------------------
# Function 2 : Train model using only 2 features
# --------------------------------------------------
def reducedModel(dataPath):

    df = pd.read_csv(dataPath)

    X = df[['StudyHours','Attendance']]
    Y = df['FinalResult']

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier()

    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    return accuracy_score(Y_test, Y_pred)


# --------------------------------------------------
# Main Function
# --------------------------------------------------
def main():
    border = "-" * 50
    dataPath = "../DataSets/student_performance_ml.csv"

    full_accuracy = fullModel(dataPath)
    reduced_accuracy = reducedModel(dataPath)

    print(border)
    print("Accuracy with all features :", full_accuracy)
    print("Accuracy with StudyHours & Attendance :", reduced_accuracy)
    print(border)

    print(border)
    if reduced_accuracy >= full_accuracy:
        print("The model still performs well using only StudyHours and Attendance.")
    else:
        print("Removing other features slightly reduces the model performance.")
    print(border)

if __name__ == "__main__":
    main()