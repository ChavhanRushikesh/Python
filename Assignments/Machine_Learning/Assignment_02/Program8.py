#Write a singie structured Python program that performs:
# 1. Dataset loading
# 2. Data analysis
# 3. Visualization
# 4. Train-test split
# 5. Model training
# 6. Prediction
# 7. Accuracy calculation
# 8. Confusion matrix generation
# 9. Final conclusion
# Your code should include proper comments explaining each step

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

def MarvellousClassifire(dataPath):

    border = "-" * 50

    # --------------------------------------------------
    # Step 1 : Load the dataset from CSV file
    # --------------------------------------------------
    print(border)
    print("Step 1 : Load the dataset from csv file")
    print(border)

    df = pd.read_csv(dataPath)

    print("Dataset loaded successfully!")
    print("First few rows of dataset:")
    print(df.head())
    print(border)

    # --------------------------------------------------
    # Step 2 : Data Analysis
    # --------------------------------------------------
    print("\nStep 2 : Data Analysis")
    print(border)

    print("\nDataset Shape:", df.shape)

    print("\nDataset Info:")
    df.info()

    print("\nDataset Description:")
    print(df.describe())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print(border)

    # --------------------------------------------------
    # Step 3 : Data Visualization
    # --------------------------------------------------

    # Histogram (Feature distribution)
    df.hist(figsize=(10,8))
    plt.suptitle("Feature Distribution")
    plt.show()

#     # Boxplot
#     sns.boxplot(x='FinalResult', y='StudyHours', data=df)
#     plt.title("StudyHours vs FinalResult")
#    # plt.show()

#     # Scatter Plot
#     plt.scatter(df['StudyHours'], df['PreviousScore'])
#     plt.xlabel("StudyHours")
#     plt.ylabel("PreviousScore")
#     plt.title("StudyHours vs PreviousScore")
#   #  plt.show()

#     # Count Plot
#     sns.countplot(x='FinalResult', data=df)
#     plt.title("Final Result Distribution")
#   #  plt.show()

#     # Correlation Heatmap
#     plt.figure(figsize=(8,6))
#     sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
#     plt.title("Correlation Heatmap")
#    # plt.show()

    # --------------------------------------------------
    # Step 4 : Train-Test Split
    # --------------------------------------------------

    X = df[['StudyHours','Attendance','PreviousScore','AssignmentsCompleted','SleepHours']]
    Y = df['FinalResult']

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42
    )

    print("\nTraining data size:", X_train.shape)
    print("Testing data size:", X_test.shape)

    # --------------------------------------------------
    # Step 5 : Model Training
    # --------------------------------------------------

    model = DecisionTreeClassifier(
        criterion="gini",
        max_depth=3,
        random_state=42
    )

    model.fit(X_train, Y_train)

    print("\nModel trained successfully.")

    # --------------------------------------------------
    # Step 6 : Prediction
    # --------------------------------------------------

    Y_pred = model.predict(X_test)

    print("\nPredicted values:")
    print(Y_pred)

    # --------------------------------------------------
    # Step 7 : Accuracy Calculation
    # --------------------------------------------------

    accuracy = accuracy_score(Y_test, Y_pred)

    print("\nModel Accuracy:", accuracy * 100, "%")

    # --------------------------------------------------
    # Step 8 : Confusion Matrix Generation
    # --------------------------------------------------

    cm = confusion_matrix(Y_test, Y_pred)

    print("\nConfusion Matrix:")
    print(cm)

    # Confusion matrix visualization
    plt.figure(figsize=(6,4))
    sns.heatmap(cm, annot=True, cmap="Blues", fmt="d",
                xticklabels=["Fail","Pass"],
                yticklabels=["Fail","Pass"])

    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")
    plt.show()

    # --------------------------------------------------
    # Step 9 : Final Conclusion
    # --------------------------------------------------

    print(border)
    print("Step 9 : Final Conclusion")
    print(border)

    if accuracy >= 0.9:
        print("The Decision Tree model performs very well on the dataset.")
    elif accuracy >= 0.7:
        print("The model performs reasonably well but can be improved.")
    else:
        print("The model performance is poor and requires improvement.")
    
    return X, model

def main():
    MarvellousClassifire("../DataSets/student_performance_ml.csv")

if __name__ == "__main__":
    main()