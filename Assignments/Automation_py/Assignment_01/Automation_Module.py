#Module with functionality to search copy writelog renamefiles and create directory!!

import os
# ------------------------------------------------------------
# Report 
# ------------------------------------------------------------

def writeLog(logFile, report):
    File = open(logFile, "a")
    File.write(report + "\n")
    File.close()

# ------------------------------------------------------------
# Scan files
# ------------------------------------------------------------

def searchFiles(directory, extension,logFile):
    if(os.path.exists(directory)):
        if(os.path.isdir(directory)):
            matchFile = []

            for folder, subfolders, files in os.walk(directory):
                for file in files:
                    if file.endswith(extension):
                        matchFile.append(os.path.join(folder, file))
                        
            return matchFile
        else:
            writeLog(logFile,"No such a directory on that path..!!")
    else:
        writeLog(logFile,"Directory Not found..!!")
        
# ------------------------------------------------------------
# Rename files
# ------------------------------------------------------------

def renameFiles(fileList, oldExt, newExt, logFile):
    for filePath in fileList:
        try:
            newPath = filePath.replace(oldExt, newExt)
            os.rename(filePath, newPath)
            writeLog(logFile,"File Renamed to : " + filePath + " : " + newPath)
        except Exception:
            writeLog(logFile,"Error during renaming file : " + filePath)

# ------------------------------------------------------------
# Copy files
# ------------------------------------------------------------

def copyFiles(mDirectory, cDirectory, logFile):
    try:
        for folder, subfolders, files in os.walk(mDirectory):
            newSubDir = folder.replace(mDirectory, cDirectory, 1)
            if not os.path.exists(newSubDir):
                os.makedirs(newSubDir)

            for file in files:
                Obj1 = os.path.join(folder, file)
                Obj2 = os.path.join(newSubDir, file)

                mFile = open(Obj1, "rb")
                data = mFile.read()
                mFile.close()

                cFile = open(Obj2, "wb")
                cFile.write(data)
                cFile.close()

                writeLog(logFile, "File Copied Successfully : " + file)

    except Exception as e:
        writeLog(logFile, "There is some issue to copy file : " + file)
        writeLog(logFile,"Exception : "+ e)

# ------------------------------------------------------------
# Create directory
# ------------------------------------------------------------

def createDirectory(cDirectory, logFile):
    try:
        if os.path.exists(cDirectory):
            writeLog(logFile, f"Directory already exists : {cDirectory}")
            return
        else :
            os.makedirs(cDirectory)
            writeLog(logFile, "Directory created : " + cDirectory)

    except Exception as e:
        writeLog(logFile, "Error while creating directory : " + cDirectory)
        writeLog(logFile,"Exception : " + e)

# ------------------------------------------------------------
# copy file from directory with Extention 
# ------------------------------------------------------------

def copyFilesWithExt(mDirectory, cDirectory, extention, logFile):
    try:
        for folder, subfolder, files in os.walk(mDirectory):
            makeDir = folder.replace(mDirectory, cDirectory, 1)
            if not os.path.exists(makeDir):
                os.makedirs(makeDir)
                writeLog(logFile, f"Directory created: {makeDir}")

            for file in files:
                if file.lower().endswith(extention.lower()):
                    Obj1 = os.path.join(folder, file)
                    Obj2 = os.path.join(makeDir, file)

                    mFile = open(Obj1, "rb")
                    data = mFile.read()
                    mFile.close()

                    cFile = open(Obj2, "wb")
                    cFile.write(data)
                    cFile.close()

                    writeLog(logFile, f"File copied successfully: {Obj2}")
    except Exception as e:
        writeLog(logFile, f"Error copying files: {str(e)}")