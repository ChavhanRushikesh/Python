#Ass  - 30
#Search a Word in File
# Problem Statement:
# Write a program which accepts a file name and a word from the user and checks whether that word is present in the file or not.
# Input:
# Demo.txt Marvellous
# Expected Output:
# Display whether the word Marvellous is found in Demo. txt or not.

import os

def searchWord(fileName, checkWord):
    count = 0
    if (os.path.exists(fileName)):
        mFile = open(fileName, "r")
        for line in mFile:
            Short = line.split()
            for Search in Short:
                if Search == checkWord:
                    return True

        mFile.close()
        return False
    else:
        print("File Not Found...!!")
       
def main():
    fName = input("Enter the file name : ")
    cWord = input("Enter the word to search : ")

    found = searchWord(fName, cWord)

    if found:
        print("The word ",cWord," is found in ",fName)
    else:
        print("The word ",cWord," is not found in ",fName)

if __name__ == "__main__":
    main()