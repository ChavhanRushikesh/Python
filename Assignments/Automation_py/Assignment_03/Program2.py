#Ass-33
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
Add Open Files Monitoring Feature For each process, display:
    Number of files opened by the process.
Requirement:
    Count open file descriptors using system/library calls
    Handle permission errors properly
Mention "Access Denied" in log if required
"""
import sys
import time
from automationModule import *

def createLog(fileName):
    Border = "-" * 50

    printLog(fileName, Border)
    printLog(fileName, "---- Open Files Monitoring Report -----")
    printLog(fileName, "Log created : " + time.ctime())
    printLog(fileName, Border)
    printLog(fileName, "------------ System Report ----------------")

    Data = processScan2()
    count = 0

    for info in Data:
        printLog(fileName, "PID : %s" % info.get("pid"))
        printLog(fileName, "Name : %s" % info.get("name"))
        printLog(fileName, "Count of open file descriptors : %s" % info.get("open_files"))
        printLog(fileName, "Timestamp : %s" % info.get("timestamp"))
        printLog(fileName, Border)
        count += 1

    printLog(fileName, "Total Number of Processes : " + str(count))
    printLog(fileName, Border)
    printLog(fileName, "------------- End Of Log File -------------")
    printLog(fileName, Border)

def main():

    Border = "-" * 50
    print(Border)
    print("----- Marvellous Open Files Monitoring Features -----")
    print(Border)

    if (len(sys.argv) == 2):
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This script is use to :")
            print("1 : Create automatic log")
            print("2 : Executes Periodically")
            print("3 : Store information about processes ")
            print("4 : Store information about Threads")

        elif sys.argv[1] == "--u" or sys.argv[1] =="--U":
            print("Use the automation script as :")
            print("ScriptName.py TimeInterval DirectoryName")
            print("DirectoryName : Name of the directory to create auto logs")

        else:
            print("Inside project logic") 
            print("Directory name : ",sys.argv[1])
            fileName = createLogFile(sys.argv[1])
            createLog(fileName)

             #Apply the Scheduler
            print("Open Files Monitoring system started successfully")
            print("Directory created with name : ",sys.argv[1])
    else:
        print("Invalid Number of Command line arguments")
        print("Unable to procced as there is no such option")
        print("Please use --h or --u to get more details")

    print(Border)
    print("--------- Thank you for using our script ---------")
    print(Border)

if __name__ == "__main__":
    main()