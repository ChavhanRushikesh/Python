# 2. Using the same dataset from above question, calculate model performance.
# Tasks
# 1. Predict all Y values using regression equation.
# 2. Calculate:
# • Mean Squared Error (MSE)
# • R2 Score
# Show all intermediate calculations.


import math 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def FunctionCheckKvalue():
    
    Border = "- "* 55
    
    print("Original Dataset ")
    data = [    
        {"Point" : "A" ,"X": 1,"Y":2,"Label":"Red"},
        {"Point" : "B" ,"X": 2,"Y":3,"Label":"Red"},
        {"Point" : "C" ,"X": 3,"Y":1,"Label":"Blue"},
        {"Point" : "D" ,"X": 6,"Y":5,"Label":"Blue"}
    ]
    
    df = pd.DataFrame(data)
    
    print(df)
    

    X = df[["X"]]   # independent variable
    Y = df["Y"]     # dependent variable
    
    print("Shape of Independent variables :",X.shape)
    print("Shape of Dependent variable ",Y.shape)

    
    print(Border)
    print(" Create & train the model ")
    print(Border)
    
    model = LinearRegression()
    
    model.fit(X,Y) # model Train using fit()
    
    print(Border)
    print(" test the model  ")
    print(Border)
    
    Ypred = model.predict(X) # Test the model
    
    print(Border)
    print(" Evaluate teh model ")
    print(Border)
    
    # Calculate the MSE (Mean Squared Error )
    MSE = mean_squared_error(Y,Ypred)
    print("Mean square Error : ",MSE)
    
    # Calculate the r2 Square 
    
    R2 = r2_score(X,Ypred)
    print("R2 Predict : ", R2)
    
def main():
    FunctionCheckKvalue()
if __name__ == "__main__":
    main()
    