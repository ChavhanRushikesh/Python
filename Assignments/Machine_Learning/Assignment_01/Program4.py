#Pass = 1
#Fail = 0

"""
Use value_counts() to analyze the distribution of FinalResult. Calculate the percentage 
of Pass and Fail students. Is the dataset balanced? Justify your answer.
"""
import pandas as pd

def main():
    file_path = '../DataSets/student_performance_ml.csv'
    data = pd.read_csv(file_path)

    final_result_counts = data['FinalResult'].value_counts()
    print("Distribution of FinalResult:")
    print(final_result_counts)

    total_students = data.shape[0]
    pass_percentage = (final_result_counts[1] / total_students) * 100
    fail_percentage = (final_result_counts[0] / total_students) * 100
    print("\nPercentage of Pass students: {:.2f}%".format(pass_percentage))
    print("Percentage of Fail students: {:.2f}%".format(fail_percentage))

    if abs(pass_percentage - fail_percentage) < 10:
        print("\nThe dataset is balanced.")
    else:
        print("\nThe dataset is imbalanced.")

if __name__ == "__main__":
    main()