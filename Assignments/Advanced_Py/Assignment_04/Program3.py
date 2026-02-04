#Ass - 30
# Display File Line by Line
# Problem Statement:
# Write a program which accepts a file name from the user and displays the contents of the file line by line on the
# screen.
# Input:
# Demo.txt
# Expected Output:
# Display each line of Demo. txt one by one.


import os

def printLines(fileName):
    if (os.path.exists(fileName)):
        file = open(fileName, "r")
        for data in file:
            print(data, end="")

        file.close()
    else:
        print("File Not Found...!!")
       
def main():
    fName = input("Enter the file name : ")
    printLines(fName)
    
if __name__ == "__main__":
    main()