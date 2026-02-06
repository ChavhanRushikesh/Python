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
Design automation script which accept directory name and two file extensions from user.
Rename all files with first file extension with the second file extenntion.

Usage: DirectoryRename.py "Demo" ".txt" ".doc"

Demo is name of directory and .txt is the extension that we want to search and rename with .doc.
After execution this script each .txt file gets renamed as .doc. as
"""
import sys
import time
from Automation_Module import searchFiles, renameFiles, writeLog

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

        directory = sys.argv[1]
        oldExt = sys.argv[2]
        newExt = sys.argv[3]

        files = searchFiles(directory, oldExt, logFile)
        renameFiles(files, oldExt, newExt, logFile)

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
