#Train model with:
#max_depth = None

#Calculate:
# Training accuracy
# Testing accuracy
# If training accuracy is 100% but testing accuracy is lower, explain why this happens

import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():
    df = pd.read_csv("../DataSets/student_performance_ml.csv")

    X = df[['StudyHours','Attendance','PreviousScore','AssignmentsCompleted','SleepHours']]
    Y = df['FinalResult']

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42
    )

    model = DecisionTreeClassifier(max_depth=None)

    model.fit(X_train, Y_train)

    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test)

    train_acc = accuracy_score(Y_train, train_pred)
    test_acc = accuracy_score(Y_test, test_pred)

    print("Training Accuracy:", train_acc * 100)
    print("Testing Accuracy:", test_acc * 100)

if __name__ == "__main__":
    main()