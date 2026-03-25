#Decision Tree Visualization
# Use:
# from sklearn.tree import plot tree
# Visualize the trained decision tree.
# Which feature appears at the root node?
# Why do you think that feature was selected first?

import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("../DataSets/student_performance_ml.csv")

    X = df[['StudyHours','Attendance','PreviousScore','AssignmentsCompleted','SleepHours']]
    Y = df['FinalResult']

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42
    )

    model = DecisionTreeClassifier()
    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)
    
    plt.figure(figsize=(10, 6))
    plot_tree(model, feature_names=X.columns, filled=True)

    plt.show()

if __name__ == "__main__":
    main()

# root is Attendance:
# Attendance appears at the root node because it creates the best split in data and reduces impurity most.

# Decision trees choose first feature based on:
# highest information gain
# or
# lowest impurity (Gini / entropy)

# So you can write:
# The root feature is selected first because it best separates the classes and gives maximum information gain.