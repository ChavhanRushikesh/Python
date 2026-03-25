#Ass-29
# Frequency of a String in File
# Problem Statement:
# Write a program which accepts a file name and one string from the user and returns the frequency (count of occurrences)
# of that string in the file.
# Input:
# Demo.txt Marvellous
# Expected Output:
# Count how many times "Marvellous" appears in Demo. txt.


import os

class fileIO:

    def __init__(self,fileName , Search):
         self.fName = fileName
         self.fSearch = Search

    def cFrequency(self):
        count = 0
        if(os.path.exists(self.fName)):
            mFile = open(self.fName, "r")
            data = mFile.read()
            mFile.close()

            count = data.count(self.fSearch)        
            return count
        
            mFile = open(self.fName, "r")
            for line in mFile:
                Short = line.split()
                for Search in Short:
                    if Search == self.fSearch:
                        count += 1

            mFile.close()
            return count
        else:
            print("File Not Found.!!")
            
def main():
    fname = input("Enter file name: ")
    search = input("Enter string to search: ")

    obj = fileIO(fname, search)
    Ret = obj.cFrequency()

    print(f"Count of {search} is: {Ret}")

if __name__ == "__main__":
    main()