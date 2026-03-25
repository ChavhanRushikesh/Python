#Pass = 1
#Fail = 0

"""
Draw a boxplot for Attendance. Identify if any outliers are present.
"""
import pandas as pd
import matplotlib.pyplot as plt

def main():
    file_path = '../DataSets/student_performance_ml.csv'
    data = pd.read_csv(file_path)

    
    plt.boxplot(data['Attendance'])
    plt.title('Boxplot of Attendance')
    plt.ylabel('Attendance')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()

