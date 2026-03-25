#Pass = 1
#Fail = 0

"""
Plot SleepHours against FinalResult. Does sleeping more guarantee success? Explain
"""
import pandas as pd
import matplotlib.pyplot as plt

def main():
    file_path = '../DataSets/student_performance_ml.csv'
    data = pd.read_csv(file_path)

    
    plt.scatter(data[data['FinalResult'] == 1]['SleepHours'], data[data['FinalResult'] == 1]['FinalResult'], color='green', label='Passed')
    plt.scatter(data[data['FinalResult'] == 0]['SleepHours'], data[data['FinalResult'] == 0]['FinalResult'], color='red', label='Failed')
    plt.title('SleepHours vs FinalResult')
    plt.xlabel('SleepHours')
    plt.ylabel('FinalResult')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()

#Does sleeping more guarantee success? Explain:-
# Sleeping more does not guarantee success. While adequate sleep is important for cognitive 
# function and overall well-being, it is just one of many factors that can influence academic 
# performance. Other factors such as study habits, attendance, previous scores, 
# and assignments completed also play significant roles in determining a student's success.
# Therefore, while getting enough sleep can contribute to better performance, it is not a
# sole determinant of success.
