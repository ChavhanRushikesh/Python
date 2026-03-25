#Generate confusion matrix using sklearn. Display it using ConfusionMatrixDisplay.

# Expiain clearly:
    # True Positive
    # True Negative
    # False Positive
    # False Negative

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import Program2 as dPredict
import matplotlib.pyplot as plt

def main():
    trainData,Y_test, Y_pred = dPredict.main()

    cm = confusion_matrix(Y_test, Y_pred)
    print("\nConfusion Matrix:")
    print(cm)

    data = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=trainData.classes_)
    data.plot()
    plt.title("Confusion matrix of iris dataset")
    plt.show()

if __name__ == "__main__":
    main()