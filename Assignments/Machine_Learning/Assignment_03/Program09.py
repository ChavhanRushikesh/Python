#Create a new column:
# PerformanceIndex = (StudyHours * 2) + Attendance
# Train the model including this new feature. Does accuracy improve?

import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():
    df = pd.read_csv("../DataSets/student_performance_ml.csv")

    df['PerformanceIndex'] = (df['StudyHours'] * 2) + df['Attendance']

    X = df[['StudyHours', 'Attendance', 'PerformanceIndex']]
    Y = df['FinalResult']

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    model = DecisionTreeClassifier()

    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    print("Accuracy:", accuracy_score(Y_test, Y_pred) * 100)

if __name__ == "__main__":
    main()
