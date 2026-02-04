#Ass-30
# Count Lines in a File
# Problem Statement:
# Write a program which accepts a file name from the user and counts how many lines are present in the file.
# Input:
# Demo.txt
# Expected Output: Total number of lines in Demo. txt.

import os

def countLines(fileName):
    count = 0
    if (os.path.exists(fileName)):
        data = open(fileName, "r")
        for _ in data:
            count += 1

        data.close()
        return count
    else:
        print("File Not Found...!!")
       
def main():
    fName = input("Enter the file name : ")
    Ret = countLines(fName)
    if Ret:
        print(f"Number of Lines in file are : {Ret}")

if __name__ == "__main__":
    main()