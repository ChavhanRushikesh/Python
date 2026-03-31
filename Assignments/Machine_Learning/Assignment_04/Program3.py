# 3. Use KNN to predict whether a student passes or fails based on study hours and attendance.
# Dataset

# Tasks
# 1. Accept input from user:
# ◦ Study hours
# ◦ Attendance percentage
# 2. Apply KNN algorithm
# 3. Predict whether the student Passes or Fails
# Input Example
# Enter Study Hours: 4
# Enter Attendance: 70
# Expected Output
# Predicted Result: Pass

import math 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

def EuclideanX(P1,P2):
    Ans = math.sqrt((P1["X"] - P2["X"])**2 + (P1["Y"] - P2["Y"])**2)
    return Ans

# Function for to check the neighbor by changing  k value and accuracy 
def FunctionCheckKvalue():
    
    border = "- "* 55
#     Study Hours    Attendance      Result
        # 2          60              Fail
        # 5          80              Pass
        # 6          85              Pass
        # 1          50              Fail
    print("Original Dataset ")
    data = [    
        {"Study_Hours" : 2,"Attendance": 60,"Result":"Fail"},
        {"Study_Hours" : 5,"Attendance": 80,"Result":"Pass"},
        {"Study_Hours" : 6 ,"Attendance": 85,"Result":"Pass"},
        {"Study_Hours" : 1 ,"Attendance": 50,"Result":"Fail"}
    ]
    
    df = pd.DataFrame(data)
    
    print(df)
    
    
    feature_column =[
        "Study_Hours",
        "Attendance"
    ]
    
    X = df[feature_column] # type: ignore
    Y = df["Result"] # type: ignore
    
    
    print("--------------------- Data Splitting -----------------")
    
    
    print("X - Independent  ", X.shape) 
    print("Y - Dependent ",Y.shape)  
    
    model = KNeighborsClassifier(n_neighbors = 3)
    
    print("---------------- Train Model -----------------")
    
    model.fit(X,Y)
    
    # USer Input 
    study_hours = float(input("Enter Study Hours: "))
    attendance = float(input("Enter Attendance: "))
    
    new_data = pd.DataFrame([[study_hours, attendance]],
                        columns=["Study_Hours","Attendance"])
    
    Prediction  = model.predict(new_data)   # type: ignore
    
    print("Predicted Result : ", Prediction)
    
    
def main():
    FunctionCheckKvalue()
if __name__ == "__main__":
    main()
    