import os

def DirectoryScanner(DirectoryName = "Marvellous"):

    Ret = os.path.exists(DirectoryName)
    if(Ret == False):
        print("There is no such directory!!..")
        return
    
    Ret = os.path.isdir(DirectoryName)
    if Ret == False:
        print("Unable to scan its not a directory!!..")
        return
    
    print("Contants of the directory are : ")
    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
        print("Folder name : ",FolderName)

        for subF in SubFolderName:
            print("SubFolder name : ",subF)

        for fName in FileName:
            print("File name : ",fName)

def main():
    DirectoryName = input("Enter the name of Directory :")
    DirectoryScanner(DirectoryName)

if __name__ == "__main__":
    main()