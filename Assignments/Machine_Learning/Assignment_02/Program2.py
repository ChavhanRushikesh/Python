#Use the trained model to predict results for X_test. 
#Display predicted values along with actual values.

import Program1 as dfit

def main():
    trainData, X_train, Y_train, X_test, Y_test = dfit.main()

    Y_pred = trainData.predict(X_test)
    
    print("Model Evaluation completed...")
    print(f"Predicted values shape: {Y_pred.shape}")
   
    print("\nPredicted vs Actual values:")
    for i in range(len(Y_pred)):
        print(f"Sample {i+1}: Predicted = {Y_pred[i]}, Actual = {Y_test.iloc[i]}")

    return trainData, Y_pred, Y_test

if __name__ == "__main__":
    main()

#iloc :- Is a powerful tool for accessing data in a DataFrame by position. When you use 
# Y_test.iloc[i], you're able to access the i-th element in the Y_test series, which 
# contains the actual values for the test set. This is particularly useful when you 
# want to compare the predicted values from your model with the actual values. 
# By iterating through the predicted values and using iloc to get the corresponding 
# actual values, you can easily display a side-by-side comparison of predictions and 
# true labels.