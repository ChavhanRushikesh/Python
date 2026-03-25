#Use the trained model to predict result for a student with:
# StudyHours = 6
# Attendance = 85
# PreviousScore =66
# AssignmentsCompleted = 7
# SleepHours = 7
# Will the student Pass or Fail?

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def StudentResult():
    data = "../DataSets/student_performance_ml.csv"
    df = pd.read_csv(data)
    print("Data loaded successfully.")

    X = df[['StudyHours','Attendance','PreviousScore','AssignmentsCompleted','SleepHours']]
    Y = df['FinalResult'] 

    model = DecisionTreeClassifier(
        criterion="gini",
        max_depth=3,       
        random_state=42  
    )
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    trainData = model.fit(X_train,Y_train)
    print("Model trained successfully.")
    
    #StudyHours=6, Attendance=85, PreviousScore=66, AssignmentsCompleted=7, SleepHours=7
    # student_data = [[6, 85, 66, 7, 7]] 
    # Y_pred = trainData.predict(student_data)
    
    student_data = pd.DataFrame([[6, 85, 66, 7, 7]],
    columns=['StudyHours','Attendance','PreviousScore','AssignmentsCompleted','SleepHours'])
    Y_pred = trainData.predict(student_data)
    
    if Y_pred[0] == 1:
        print("The student is predicted to Pass.")
    else:
        print("The student is predicted to Fail.")
def main():
    StudentResult()

if __name__ == "__main__":
    main()

