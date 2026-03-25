#Calculate model accuracy using accuracy_score. Display the result in percentage format.

import Program2 as dPredict
from sklearn.metrics import accuracy_score

def main():
    trainData, Y_pred, Y_test = dPredict.main()
    accuracy = accuracy_score(Y_test, Y_pred)
    print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

if __name__ == "__main__":
    main()