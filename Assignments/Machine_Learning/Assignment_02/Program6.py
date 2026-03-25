# Train three Decision Tree models with:
# max_depth = 1
# max_depth = 3
# max_depth = None
# Compare their testing accuracies and write your observations.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import Program1 as pgm1
from sklearn.metrics import accuracy_score

def maxDepth_1():
    data = "../DataSets/student_performance_ml.csv"
    df = pd.read_csv(data)
    print("Data loaded successfully.")

    X = df[['StudyHours','Attendance','PreviousScore','AssignmentsCompleted','SleepHours']]
    Y = df['FinalResult'] 

    model = DecisionTreeClassifier(
        criterion="gini",
        max_depth=1,       
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
    Y_pred = trainData.predict(X_test)
    accuracy = accuracy_score(Y_test, Y_pred)
    print(f"Testing Accuracy with max_depth=1: {accuracy * 100}%")
   
def maxDepth_3():
    trainData, X_train, Y_train, X_test, Y_test = pgm1.main()
    Y_pred = trainData.predict(X_test)
    accuracy = accuracy_score(Y_test, Y_pred)
    print(f"Testing Accuracy with max_depth=3: {accuracy * 100}%")

def maxDepth_None():
    data = "../DataSets/student_performance_ml.csv"
    df = pd.read_csv(data)
    print("Data loaded successfully.")

    X = df[['StudyHours','Attendance','PreviousScore','AssignmentsCompleted','SleepHours']]
    Y = df['FinalResult'] 

    model = DecisionTreeClassifier(
        criterion="gini",
        max_depth=None,       
        random_state=42  
    )
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, 
        Y,
        test_size=0.2,         
        random_state=42         
    )
    trainData =model.fit(X_train,Y_train)
    print("Model trained successfully.")
    Y_pred = trainData.predict(X_test)
    accuracy = accuracy_score(Y_test, Y_pred)
    print(f"Testing Accuracy with max_depth=None: {accuracy * 100}%")

def main():
    border = "=" * 50   
    print(border)
    print("Using max_depth = 1:")
    print(border)
    maxDepth_1()

    print(border)
    print("Using max_depth = 3:")
    print(border)
    maxDepth_3()

    print(border)
    print("Using max_depth = None:")
    print(border)
    maxDepth_None()

if __name__ == "__main__":
    main()


#Observations:
#1. The testing accuracy with max_depth=1 is relatively low, indicating that the model
#   is underfitting the data and not capturing the underlying patterns effectively.
#2. The testing accuracy with max_depth=3 is higher than that of max_depth=1, suggesting 
#   that the model is better at capturing the patterns in the data without overfitting.
#3. The testing accuracy with max_depth=None is the highest among the three, indicating that
#   the model is able to capture the most complex patterns in the data. However, it may also be
#   at risk of overfitting, especially if the dataset is small or noisy.
#4. Overall, the choice of max_depth has a significant impact on the model's performance, and 
#   it is important to find a balance between underfitting and overfitting when selecting this 
#   hyperparameter.
