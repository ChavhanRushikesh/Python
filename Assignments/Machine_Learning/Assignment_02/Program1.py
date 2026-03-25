#Import DecisionTreeClassifier from sklearn. Create a model object and train it using fit().

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

def main():
    data = "../DataSets/student_performance_ml.csv"
    df = pd.read_csv(data)
    print("Data loaded successfully.")

    X = df[['StudyHours','Attendance','PreviousScore','AssignmentsCompleted','SleepHours']]
    Y = df['FinalResult'] 

    model = DecisionTreeClassifier(
        criterion="gini",
        max_depth=3,        #5
        random_state=42  
    )
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, 
        Y,
        test_size=0.2,          #0.5
        random_state=42         #use to shuffel data
    )
    trainData =model.fit(X_train,Y_train)
    print("Model trained successfully.")
    return trainData, X_train, Y_train, X_test, Y_test

if __name__ == "__main__":
    main()