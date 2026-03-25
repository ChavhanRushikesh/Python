#Pass = 1
#Fail = 0

"""
Based on the dataset values, analyze whether:
Higher StudyHours increase the chance of passing.
Higher Attendance improves FinalResult. Write your observations in 4-5 lines.
"""
import pandas as pd

def main():
    file_path = '../DataSets/student_performance_ml.csv'
    data = pd.read_csv(file_path)

    study_hours_passed = data[data['FinalResult'] == 1]['StudyHours']
    study_hours_failed = data[data['FinalResult'] == 0]['StudyHours']

    average_study_hours_passed = study_hours_passed.mean()
    average_study_hours_failed = study_hours_failed.mean()

    print("Average StudyHours for Passed students:", average_study_hours_passed)
    print("Average StudyHours for Failed students:", average_study_hours_failed)

    attendance_passed = data[data['FinalResult'] == 1]['Attendance']
    attendance_failed = data[data['FinalResult'] == 0]['Attendance']

    average_attendance_passed = attendance_passed.mean()
    average_attendance_failed = attendance_failed.mean()

    print("Average Attendance for Passed students:", average_attendance_passed)
    print("Average Attendance for Failed students:", average_attendance_failed)

if __name__ == "__main__":
    main()
    
# Observations:
# 1. The average StudyHours for students who passed is higher than that of students who
#    failed, suggesting that higher StudyHours may increase the chance of passing.
# 2. The average Attendance for students who passed is also higher than that of students
#    who failed, indicating that higher Attendance may improve FinalResult.
# 3. Both StudyHours and Attendance appear to be positively correlated with passing the
#    course, but further analysis would be needed to determine causation.
# 4. It is important to consider other factors such as PreviousScore and SleepHours
#    that may also influence the FinalResult.


