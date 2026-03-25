#Pass = 1
#Fail = 0

"""
Write a Python program to load the file student_performance_ml. csv using pandas.
Display:
    First 5 records
    Last 5 records
    Total number of rows and columns
    List of column names
    Data types of each column
"""
import pandas as pd

def main():
    file_path = "../DataSets/student_performance_ml.csv"
    data = pd.read_csv(file_path)

    print("First 5 records:")
    print(data.head())
 
    print("\nLast 5 records:")
    print(data.tail())
  
    print("\nTotal number of rows and columns:")
    print(data.shape)
    
    print("\nList of column names:")
    print(data.columns)
   
    print("\nData types of each column:")
    print(data.dtypes)

if __name__ == "__main__":
    main()