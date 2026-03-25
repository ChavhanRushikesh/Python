#Train model using:
# random_state 0
# random state = 10
# random state 42
# Compare testing accuracy. Does the result change?

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def randomState_0(dataPath):
    df = pd.read_csv(dataPath)

    X = df[['StudyHours','Attendance','PreviousScore','AssignmentsCompleted','SleepHours']]
    Y = df['FinalResult']

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42
    )

    model = DecisionTreeClassifier()
    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)
    accuracy = accuracy_score(Y_test, Y_pred)
    return accuracy

def randomState_10(dataPath):
    df = pd.read_csv(dataPath)

    X = df[['StudyHours','Attendance','PreviousScore','AssignmentsCompleted','SleepHours']]
    Y = df['FinalResult']

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42
    )

    model = DecisionTreeClassifier()
    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)
    accuracy = accuracy_score(Y_test, Y_pred)
    return accuracy

def randomState_42(dataPath):
    df = pd.read_csv(dataPath)

    X = df[['StudyHours','Attendance','PreviousScore','AssignmentsCompleted','SleepHours']]
    Y = df['FinalResult']

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42
    )

    model = DecisionTreeClassifier()
    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)
    accuracy = accuracy_score(Y_test, Y_pred)
    return accuracy

def MarvellousTreeClassifire(dataPath):
    rs42 = randomState_42(dataPath)
    rs0 = randomState_0(dataPath)
    rs10 = randomState_10(dataPath)
    print("Random state 42 : ", rs42)
    print("Random state 0 : ", rs0)
    print("Random state 10 : ", rs10)

def main():
    MarvellousTreeClassifire("../DataSets/student_performance_ml.csv")

if __name__ == "__main__":
    main()