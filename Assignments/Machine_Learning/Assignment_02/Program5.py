#Calculate:
#   Training accuracy
#   Testing accuracy
#   Compare both and comment whether the model is overfitting or underfitting.

from sklearn.metrics import accuracy_score
import Program1 as dfit

def main():
    trainData, X_train, Y_train, X_test, Y_test = dfit.main()
    
    Y_pred_train = trainData.predict(X_train)
    Y_pred_test = trainData.predict(X_test)
    
    # Calculate accuracies
    training_accuracy = accuracy_score(Y_train, Y_pred_train)
    testing_accuracy = accuracy_score(Y_test, Y_pred_test)
    
    print(f"Training Accuracy: {training_accuracy:.2f}")
    print(f"Testing Accuracy: {testing_accuracy:.2f}")
    
    # Compare and comment
    if training_accuracy > testing_accuracy + 0.1:  
        print("The model appears to be overfitting (high training accuracy, lower testing accuracy).")
    elif training_accuracy < 0.6 and testing_accuracy < 0.6: 
        print("The model appears to be underfitting (low accuracies on both training and testing).")
    else:
        print("The model seems balanced (similar accuracies on training and testing).")


if __name__ == "__main__":
    main()