#Pass = 1
#Fail = 0

"""
Create a scatter plot of: StudyHours vs PreviousScore
Use different colors for Pass and Fail students.
"""
import pandas as pd

def main():
    file_path = '../DataSets/student_performance_ml.csv'
    data = pd.read_csv(file_path)

    import matplotlib.pyplot as plt
    plt.scatter(data[data['FinalResult'] == 1]['StudyHours'], data[data['FinalResult'] == 1]['PreviousScore'], color='green', label='Passed')
    plt.scatter(data[data['FinalResult'] == 0]['StudyHours'], data[data['FinalResult'] == 0]['PreviousScore'], color='red', label='Failed')
    plt.title('StudyHours vs PreviousScore')
    plt.xlabel('StudyHours')
    plt.ylabel('PreviousScore')
    plt.legend()

    plt.xlabel('StudyHours')
    plt.ylabel('Frequency')
    plt.grid(axis='y', alpha=0.75)
    plt.show()

if __name__ == "__main__":
    main()