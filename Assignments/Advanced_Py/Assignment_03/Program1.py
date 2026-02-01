# Ass-29
# Check File Exists in Current Directory
# Problem Statement:
# Write a program which accepts a file name from the user and checks whether that file exists in the current
# directory or not.
# Input: Demo.txt
# Expected Output: Display whether Demo. txt exists or not.


import os

class fileIO:
    def __init__(self):
        FileName = input("Enter the name of file : ")
        if(os.path.exists(FileName)):
            print("file is Exist..!!")
        else:
            print("File is Not Exist..!!")

def main():
    fileIO()

if __name__ == "__main__":
    main()