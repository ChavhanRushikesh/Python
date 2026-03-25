#Identify students where:
# y_test != y pred
# Display those rows.
# How many students were misclassified?
# What common pattern do you observe?

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

def studentIndenty(Y_test, Y_pred):
    count = 0

    for i in range(len(Y_test)):
        if Y_test.iloc[i] != Y_pred[i]:
            print("Row", i)
            print(Y_test.iloc[i])
            print("Actual:", Y_test.iloc[i])
            print("Predicted:", Y_pred[i])
            count += 1

    print("Total Misclassified:", count)


def MarvellousTreeClassifire(dataPath):

    df = pd.read_csv(dataPath)

    X = df[['StudyHours','Attendance','PreviousScore','AssignmentsCompleted','SleepHours']]
    Y = df['FinalResult']

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42
    )

    model = DecisionTreeClassifier()
    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)
    
    studentIndenty(Y_test, Y_pred)

def main():
    MarvellousTreeClassifire("../DataSets/student_performance_ml.csv")

if __name__ == "__main__":
    main()