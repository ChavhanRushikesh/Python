#Ass - 31
#/////////////////////////////////////////////////////////////////////////////////////////////
#
#   Please follow below rules while designing automation script as:
#       * Accept input through command line or through file.
#       * Display any message in log file instead of console.
#       * For separate task define separate function.
#       * For robustness handle every expected exception.
#       * Perform validations before taking any action.
#       * Create user defined modules to store the functionality.
#
#/////////////////////////////////////////////////////////////////////////////////////////////
"""
Design automation script which accept two directory names and one file extension. 
Copy all files with the specified extension from first directory into second directory. 
Second directory should be created at run time.

Usage: DirectoryCopyExt.py "Demo" "Temp" ".exe"

Demo is name of directory which is existing and contains files in it.
We have to create new Directory as Temp and copy all files with extension.exe from Demo to Temp.
"""

import os
import sys
import time
from Automation_Module import createDirectory, copyFilesWithExt, writeLog

def main():
    border = "-" * 65
    print(border)
    print("--------------------- Rjs Directory Automation ------------------")
    print(border)

    logFile = "AutomationReports.log"

    try:
        writeLog(logFile, border)
        writeLog(logFile,"---------------------- Automation Report ------------------------")
        writeLog(logFile, border)

        mDirectory = sys.argv[1]
        cDirectory = sys.argv[2]
        extention = sys.argv[3]

        if not os.path.exists(mDirectory):
            writeLog(logFile, f"Source directory does not exist: {mDirectory}")
            return

        createDirectory(cDirectory, logFile)
        copyFilesWithExt(mDirectory, cDirectory, extention, logFile)

    except IndexError:
        writeLog(logFile,"Invalid Numbers of Arguments")

    except Exception as e:
        print(f"Exception : ",e)

    finally:
        writeLog(logFile, border)
        writeLog(logFile, "--------- Thank you for using Rjs Directory_Automation ----------")
        writeLog(logFile, border)
        writeLog(logFile, f"------------ Report Time : {time.ctime()} -------------")
        writeLog(logFile, border)
        writeLog(logFile, "* " * 33)
        writeLog(logFile," ")

if __name__ == "__main__":
    main()
