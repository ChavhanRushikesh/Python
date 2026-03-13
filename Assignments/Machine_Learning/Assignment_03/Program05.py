#Without using accuracy_score, manually calculate accuracy:
# Verify whether it matches sklearn accuracy.

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def accuracyScore(Y_test, Y_pred):
    count = 0

    for i in range(len(Y_test)):
        if Y_test.iloc[i] == Y_pred[i]:
            count += 1

    accuracy = (count / len(Y_test)) * 100

    print("Accuracy  Score of my won function : ", accuracy)

    return accuracy

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
    InbuildFun = accuracy_score(Y_test, Y_pred) * 100
    print("accuracy of inbuild function : ",InbuildFun)

    MySelf = accuracyScore(Y_test, Y_pred)

    if MySelf == InbuildFun:
        print("Both Manual and Inbuilt accuracy functions are same ..!!")

    else:
        print("Both Manual and Inbuilt accuracy functions are different ..!!")

def main():
    MarvellousTreeClassifire("../DataSets/student_performance_ml.csv")

if __name__ == "__main__":
    main()