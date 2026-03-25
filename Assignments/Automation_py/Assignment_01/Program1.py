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

# Create user defined modules to store the functionality.
# Design automation script which accept directory name and file extension from user. Display all
# files with that extension.
# Usage: python Program1.py "Demo" ".txt"
# Demo is name of directory and .txt is the extension that we want to search.

import sys
import time
from Automation_Module import searchFiles , writeLog

def main():
    border = "-" * 65
    print(border)
    print("--------------------- Rjs Directory Automation ------------------")
    print(border)

    logFile = "AutomationReports.log"

    writeLog(logFile,border)
    writeLog(logFile,"---------------------- Automation Report ------------------------")
    writeLog(logFile,border)
    try:
        if(len(sys.argv) != 3):
            writeLog(logFile,"Invalid number of arguments.!!")
            writeLog(logFile,"Plese specify the name of directory and extention of file to search.!!")
            return
        
        directory = sys.argv[1]
        extension = sys.argv[2]

        files = searchFiles(directory, extension, logFile)

        if files:
            writeLog(logFile,f"Files with {extension} extension in {directory} :")
            for data in files:
                writeLog(logFile,data)
        else:
            writeLog(logFile,f"No files with {extension} found in {directory}.!!")

    except Exception as e:
        writeLog(logFile,"Exception : " + e)

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