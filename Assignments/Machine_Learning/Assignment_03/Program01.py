#After training the Decision Tree model, use:
# model.feature importances
# Display importance score of each feature.
# Which feature contributes the most in predicting FinalResult?
# Which feature contributes the least?

import os
import sys
sys.path.append(os.path.abspath(".."))
from Assignment_02.Program8 import MarvellousClassifire

def MarvellousTreeClassifire():

    X,model = MarvellousClassifire("../DataSets/student_performance_ml.csv")

    print("\nFeature Importance:")
    for feature, importance in zip(X.columns, model.feature_importances_):
        print(feature, ":", importance)

def main():
    MarvellousTreeClassifire()

if __name__ == "__main__":
    main()

"""Feature Importance:
StudyHours : 0.0
Attendance : 1.0
PreviousScore : 0.0
AssignmentsCompleted : 0.0
SleepHours : 0.0"""