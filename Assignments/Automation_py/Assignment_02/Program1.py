#Ass-32
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
Design automation script which accept directory name and display checksum of all files.
Usage: DirectoryChecksum.py "Demo"
"""
import sys
import time
from AutomationModule import calculateChecksum, writeLog

def main():
    border = "-" * 65
    print(border)
    print("--------------------- Rjs Directory Automation ------------------")
    print(border)

    logFile = "AutomationReports.log"
    try:
        writeLog(logFile,border)
        writeLog(logFile,"---------------------- Automation Report ------------------------")
        writeLog(logFile,border)

        if len(sys.argv) != 2:
            writeLog(logFile,"Invalid number of arguments.!!")
            writeLog(logFile,"Plese specify the name of directory and extention of file to search.!!")
            return

        directory_name = sys.argv[1]
        calculateChecksum(directory_name,logFile)

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