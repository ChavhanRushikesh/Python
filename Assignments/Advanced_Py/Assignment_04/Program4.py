#Ass  - 30
# Copy File Contents into Another File
# Problem Statement:
# Write a program which accepts two file names from the user.
# First file is an existing file
# Second file is a new file
# Copy all contents from the first file into the second file
# Input:
# ABC.txt Demo.txt
# Expected Output:
# Contents of ABC.txt copied into Demo.txt.


import os

def printLines(existingFile, newFile):
    if (os.path.exists(existingFile)):
        mFile = open(existingFile, "r")
        cFile = open(newFile,"w")

        for copy in mFile:
            cFile.write(copy)

        mFile.close()
        cFile.close()
        print("File is copied succesfully to Demo.txt!!")
    else:
        print("File Not Found...!!")
       
def main():
    eFile = input("Enter the Existing File name : ")
    newFile = input("Enter the New file name where to Copy : ")
    printLines(eFile,newFile)
    
if __name__ == "__main__":
    main()