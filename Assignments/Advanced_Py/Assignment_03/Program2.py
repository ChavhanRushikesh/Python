#Ass-29
# Display File Contents
# Problem Statement:
# Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the
# console. Input: Demo.txt Display contents of Demo. txt on console.

import os

class fileIO:
    def __init__(self):
        fileName = input("Enter the name of file : ")

        if(os.path.exists(fileName)):
            fObj = open("Demo.txt")
            data = fObj.read()
            print("Data From file is :",data)
        else:
            print("File is Not Exist..!!")
            
def main():
    fileIO()

if __name__ == "__main__":
    main()