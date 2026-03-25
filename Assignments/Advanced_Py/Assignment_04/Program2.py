#Ass-30
#Count Words in a File
# Problem Statement:
# Write a program which accepts a file name from the user and counts the total number of words in that file.
# Input:
# Demo.txt
# Expected Output: Total number of words in Demo. txt

import os

def countWords(fileName):
    count = 0
    if (os.path.exists(fileName)):
        file = open(fileName, "r")
        for data in file:
            words = data.split()
            count = count + len(words)

        file.close()
        return count
    else:
        print("File Not Found...!!")
       
def main():
    fName = input("Enter the file name : ")
    Ret = countWords(fName)
    if Ret:
        print(f"Number of Words in file are : {Ret}")

if __name__ == "__main__":
    main()