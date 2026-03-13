# Remove the column SleepHours from the dataset.
# Train the model again.
# Compare new accuracy with previous accuracy.
# Does removing this feature affect performance?

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# --------------------------------------------------
# Function 1 : Train model with SleepHours
# --------------------------------------------------
def withSleepHours(dataPath):

    df = pd.read_csv(dataPath)

    X = df[['StudyHours','Attendance','PreviousScore','AssignmentsCompleted','SleepHours']]
    Y = df['FinalResult']

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier()

    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    accuracy = accuracy_score(Y_test, Y_pred)

    return accuracy


# --------------------------------------------------
# Function 2 : Train model without SleepHours
# --------------------------------------------------
def withoutSleepHours(dataPath):

    df = pd.read_csv(dataPath)

    X = df[['StudyHours','Attendance','PreviousScore','AssignmentsCompleted']]
    Y = df['FinalResult']

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier()

    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    accuracy = accuracy_score(Y_test, Y_pred)

    return accuracy

def main():
    border = "-" * 50
    dataPath = "../DataSets/student_performance_ml.csv"

    obj1 = withSleepHours(dataPath)
    obj2 = withoutSleepHours(dataPath)
    print(border)
    print("Accuracy with SleepHours :", obj1)
    print("Accuracy without SleepHours :", obj2)
    print(border)
    
    print(border)
    if obj1 > obj2:
        print("Model performs better when SleepHours feature is included.")
    
    elif obj2 > obj1:
        print("Model performs better after removing SleepHours feature.")
    
    else:
        print("Removing SleepHours does not affect model performance.")

    print(border)

if __name__ == "__main__":
    main()