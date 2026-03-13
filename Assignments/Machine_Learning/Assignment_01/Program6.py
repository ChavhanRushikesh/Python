#Pass = 1
#Fail = 0

"""
Plot a histogram of StudyHours. Explain what the distribution tells you.
"""
import pandas as pd
import matplotlib.pyplot as plt

def main():
    file_path = '../DataSets/student_performance_ml.csv'
    data = pd.read_csv(file_path)

    plt.hist(data['StudyHours'], bins=10, edgecolor='black')
    plt.title('Distribution of StudyHours')
    plt.xlabel('StudyHours')
    plt.ylabel('Frequency')
    plt.grid(axis='y', alpha=0.75)
    plt.show()

if __name__ == "__main__":
    main()