#Automation module for checksum verification and file operations

import hashlib
import os

# ------------------------------------------------------------
# write log to file 
# ------------------------------------------------------------

def writeLog(logFile, report):
    File = open(logFile, "a")
    File.write(report + "\n")
    File.close()

# ------------------------------------------------------------
# calculate checksum of a file
# ------------------------------------------------------------

def calculateChecksum(directory_name,LogFile):

    if not os.path.exists(directory_name):
        writeLog(LogFile,"There is no such directory")
        return

    if not os.path.isdir(directory_name):
        writeLog(LogFile,"It is not a directory")
        return

    
    for folder, subfolders, files in os.walk(directory_name):
        for fname in files:
            mfile = os.path.join(folder, fname)

            hobj = hashlib.md5()
            fobj = open(mfile, "rb")

            buffer = fobj.read(1024)
            while buffer:
                hobj.update(buffer)
                buffer = fobj.read(1024)

            fobj.close()

            checksum = hobj.hexdigest()
            writeLog(LogFile,f"File Name : {mfile} and Checksum : {checksum}")

# ------------------------------------------------------------
# Find duplicate files
# ------------------------------------------------------------

def findDuplicates(directory_name,LogFile):

    if not os.path.exists(directory_name):
        writeLog(LogFile,"Directory does not exist")
        return

    if not os.path.isdir(directory_name):
        writeLog(LogFile,"Provided name is not a directory")
        return

    checksum_dict = {}

    for foldername, subfolders, filenames in os.walk(directory_name):
        for fname in filenames:
            mFile = os.path.join(foldername, fname)

            hobj = hashlib.md5()
            fobj = open(mFile, "rb")

            buffer = fobj.read(1024)
            while buffer:
                hobj.update(buffer)
                buffer = fobj.read(1024)

            fobj.close()

            checksum = hobj.hexdigest()

            if checksum in checksum_dict:
                checksum_dict[checksum].append(mFile)
            else:
                checksum_dict[checksum] = [mFile]

    for checksum in checksum_dict:
        files = checksum_dict[checksum]
        if len(files) > 1:
            writeLog(LogFile,"Duplicate files:")
            for file in files:
                writeLog(LogFile,file)
            writeLog(LogFile,"")

    writeLog(LogFile,"Duplicate file names written to AutomationReports.log")

# ------------------------------------------------------------
# Remove duplicate files
# ------------------------------------------------------------
    
def removeDuplicates(directory_name,logFile):

    if not os.path.exists(directory_name):
        writeLog(logFile,"Directory does not exist")
        return

    if not os.path.isdir(directory_name):
        writeLog(logFile,"Provided name is not a directory")
        return

    checksum_dict = {}

    for foldername, subfolders, filenames in os.walk(directory_name):
        for fname in filenames:
            mFile = os.path.join(foldername, fname)

            hobj = hashlib.md5()
            fobj = open(mFile, "rb")

            buffer = fobj.read(1024)
            while buffer:
                hobj.update(buffer)
                buffer = fobj.read(1024)

            fobj.close()

            checksum = hobj.hexdigest()

            if checksum in checksum_dict:
                checksum_dict[checksum].append(mFile)
            else:
                checksum_dict[checksum] = [mFile]

    deleted_count = 0

    for checksum in checksum_dict:
        file_list = checksum_dict[checksum]

        if len(file_list) > 1:
            for i in range(1, len(file_list)):
                try:
                    os.remove(file_list[i])
                    writeLog(logFile,file_list[i])
                    deleted_count += 1
                except:
                    writeLog(logFile,"Failed to delete: " + file_list[i])

    writeLog(logFile,f"Duplicate files deleted: {deleted_count}")
    writeLog(logFile,"Log file created as AutomationReports.log")

