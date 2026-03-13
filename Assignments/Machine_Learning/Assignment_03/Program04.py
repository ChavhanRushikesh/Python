#Create a new DataFrame with details of 5 new students. Use the trained model to predict their results. 
#Display predictions clearly.
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd


def MarvellousTreeClassifire(dataPath):

    df = pd.read_csv(dataPath)

    X = df[['StudyHours','Attendance','PreviousScore','AssignmentsCompleted','SleepHours']]
    Y = df['FinalResult']

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42
    )

    model = DecisionTreeClassifier()
    model.fit(X_train, Y_train)

    # --------------------------------------------------
    # Create DataFrame for 5 new students
    # --------------------------------------------------
    data = pd.DataFrame({

        'StudyHours':[2,5,7,3,6],
        'Attendance':[99,85,92,70,88],
        'PreviousScore':[84,60,75,50,68],
        'AssignmentsCompleted':[3,6,8,4,7],
        'SleepHours':[8,6,7,5,7]
    })

    Y_pred = model.predict(data)

    data['Result'] = Y_pred
    print(data.to_string(index=False))

def main():
    MarvellousTreeClassifire("../DataSets/student_performance_ml.csv")

if __name__ == "__main__":
    main()