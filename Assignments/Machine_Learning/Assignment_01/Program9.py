#Pass = 1
#Fail = 0

"""
Create a plot showing relationship between AssignmentsCompleted and FinalResult.
Explain your observation.
"""
import pandas as pd
import matplotlib.pyplot as plt

def main():
    file_path = '../DataSets/student_performance_ml.csv'
    data = pd.read_csv(file_path)

    plt.scatter(data[data['FinalResult'] == 1]['AssignmentsCompleted'], data[data['FinalResult'] == 1]['FinalResult'], color='green', label='Passed')
    plt.scatter(data[data['FinalResult'] == 0]['AssignmentsCompleted'], data[data['FinalResult'] == 0]['FinalResult'], color='red', label='Failed')
    plt.title('AssignmentsCompleted vs FinalResult')
    plt.xlabel('AssignmentsCompleted')
    plt.ylabel('FinalResult')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()

