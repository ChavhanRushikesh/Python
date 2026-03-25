#Ass-29
# Copy File Contents into a New File(Command Line)
# Problem Statement:
# Write a program which accepts an existing file name through command line arguments, 
# creates a new file named Demo.txt, and copies all contents from the given file into Demo.txt.
# Input (Command Line): ABC.txt
# Expected Output:
# Create Demo.txt and copy contents of ABC.txt into Demo.txt

import sys

class fileHandle:

    def copyOneToAnother(self,fileName):

        mFile = open(fileName, "r")
        cFile = open("Demo.txt","w")

        for copy in mFile:
            cFile.write(copy)

        mFile.close()
        cFile.close()
        print("File is copied succesfully to Demo.txt!!")

def main():
    obj = fileHandle()
    fileName = sys.argv[1]
    obj.copyOneToAnother(fileName)

if __name__ == "__main__":
    main()