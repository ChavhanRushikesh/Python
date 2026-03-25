#Pass = 1
#Fail = 0

"""
Using pandas functions, calculate and display:
    Average StudyHours
    Average Attendance
    Maximum PreviousScore
    Minimum SleepHours
"""
import pandas as pd

def main():
    file_path = '../DataSets/student_performance_ml.csv'
    data = pd.read_csv(file_path)

    average_study_hours = data['StudyHours'].mean()
    print("Average StudyHours:", average_study_hours)

    average_attendance = data['Attendance'].mean()
    print("Average Attendance:", average_attendance)

    max_previous_score = data['PreviousScore'].max()
    print("Maximum PreviousScore:", max_previous_score)

    min_sleep_hours = data['SleepHours'].min()
    print("Minimum SleepHours:", min_sleep_hours)

if __name__ == "__main__":
    main()
