# Dataset contains multiple records about the customers who invest in multiple advertisement
# options.
# Depends on that sales feature indicates the the increased amount in there sales


# This data set contains 4 features as
# TV
# Radio
# Television
# Depends on the above three features Sales feature indicates the increased sale amount.

# We have to design Machine Learning application which uses Classification
# technique.

# Design machine learning application which follows below steps as


# Step 1:
    # Get Data
        # Load data from Advertising.csv file into python application.
# Step 2:
    # Clean, Prepare and Manipulate data
        # As we want to use the above data into machine learning application we have prepare
        # that in the format which is accepted by the algorithms.
# Step 3:
    # Train Data
        # Now we want to train our data for that we have to select the Machine learning algorithm.
        # For that we select Linear Regression algorithm from sykit learn library.
        # For training purpose divide the dataset into half part.
        # Use train method to train our dataset.
# Step 4:
    # Test the data
        # Test data by passing the remaining half part of the data set.
# Step 5:
    # Display predicted values of Linear regression algorithms as well as expected values
    # which are provided by the data set.


import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def LinearRegressionModelTrain():
    
    Border = "- " * 40 
    
    print("Step 1 : Load the data from csv")
    print(Border)
    
    df = pd.read_csv("../DataSets/Advertising.csv")
    
    print("\n --- Some Data from csv : ---- \n")
    print(df.head())
    
    
    print(Border)
    
    print("\nStep 2 : Clean Prepare and manipulate teh data and remove unwanted columns  \n")
    
    print("Columns before delete : ",df.shape)
    
    if "Unnamed: 0" in df.columns:
        df.drop(columns=["Unnamed: 0"],inplace=True)
    
    print(Border)
    print("Columns after delete  : ", df.shape)
    print(Border)
    
    print("\n Step 3 : --- Check is any null values --- \n ")
    
    print(Border)
    print("Check if the any column contain null values ")
    print(Border) 
    print(df.isnull().sum())
    
    print(Border)
    
    print(" Step 4 : Split data to dependent and independent variable  ")
    
    print(Border)
    X = df[["TV","radio","newspaper"]]
    Y = df['sales']
    
    print("Independent Variable (X) : ",X.shape)
    print("Dependent Variable (Y) : ",Y.shape)
    
    print(Border)
    
    print("Step 5 : Split Data into training and testing 80% for training 20% for testing ")
    
    print(Border)
    
    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state= 42
    )
    
    print("\n ---- Create the model ---- \n")
    
    model = LinearRegression()
    
    print("\n ---- Train the model ---- \n")
    
    model.fit(X_train,Y_train)
    
    print("\n ---- Test the model ---- \n")
    
    Ypred = model.predict(X_test)
    
    # print("\n Predicted Values : \n", Ypred)
    
    # print("\n Expected Values : \n", Y_test)
    
    result = pd.DataFrame({
        "Actual Values : " :  Y_test.values,
        "Predicted Values ": Ypred
    })
    
    print(result)
    
def main():
    LinearRegressionModelTrain()

if __name__ == "__main__":
    main()