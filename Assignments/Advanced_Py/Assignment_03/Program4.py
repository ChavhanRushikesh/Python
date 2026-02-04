#Ass-29
# Compare Two Files (Command Line)
# Problem Statement:
# Write a program which accepts two file names through command line arguments and compares the contents of both files.
# If both files contain the same contents, display Success
# Otherwise display Failure
# Input (Command Line): Demo.txt Hello.txt
# Expected Output: Success OR Failure


import sys
import hashlib

class fileIO:
    def __init__(self):
        print("-" * 50)

        Obj1 = open(sys.argv[1],"r")
        Obj2 = open(sys.argv[2],"r")

        if Obj1.read() == Obj2.read():
            print("Both files have same contents!!")
        else:
            print("Both files are not have same contents")

        Obj1.close()
        Obj2.close()

        print("-" * 50)
        
class usingChecksum(fileIO):

    def __init__(self):
        super().__init__()

        Obj1 = open(sys.argv[1],"rb")
        Obj2 = open(sys.argv[2],"rb")

        hObj1 = hashlib.md5()
        hObj2 = hashlib.md5()

        Buffer = Obj1.read(1024)
        while(len(Buffer) > 0):
            hObj1.update(Buffer)
            Buffer = Obj1.read(1024)

        Obj1.close()

        Buffer = Obj2.read(1024)
        while(len(Buffer) > 0):
            hObj2.update(Buffer)
            Buffer = Obj2.read(1024)

        Obj2.close()
        checkSum1 = hObj1.hexdigest()
        checkSum2 = hObj2.hexdigest()

        print(f"checksum for file {sys.argv[1]} is  :",checkSum1)
        print(f"checksum for file {sys.argv[2]} is :",checkSum2)

        print("-" * 50)

        if checkSum1 == checkSum2:
            print("Success!!")
        else:
            print("Failure!!")

        print("-" * 50)

def main():
    usingChecksum()

if __name__ == "__main__":
    main()