#Pass = 1
#Fail = 0

"""
Write a program to:
    Display total number of students in the dataset
    Count how many students Passed (FinalResult = 1)
    Count how many students Failed (FinalResult = 0)
"""
import pandas as pd

def main():
    file_path = "../DataSets/student_performance_ml.csv"
    data = pd.read_csv(file_path)

    total_students = data.shape[0]
    print("Total number of students in the dataset:", total_students)

    passed_students = data[data['FinalResult'] == 1].shape[0]
    print("Number of students who Passed (FinalResult = 1):", passed_students)

    failed_students = data[data['FinalResult'] == 0].shape[0]
    print("Number of students who Failed (FinalResult = 0):", failed_students)

if __name__ == "__main__":
    main()
