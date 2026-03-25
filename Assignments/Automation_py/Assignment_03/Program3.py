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
Add Actual Memory Allocation Feature:-
    Display real memory usage of each process:-
        RSS (Resident Set Size - actual RAM used)
        VMS (Virtual Memory)
        Memory Percentage

    Requirement:-
        Show:
            Top 10 memory consuming processes
"""
import sys
import time
from automationModule import *

def createMemoryLog(fileName):
    Border = "-" * 50

    printLog(fileName, Border)
    printLog(fileName, "--------------- Memory Usage Report --------------")
    printLog(fileName, "----- Log created : " + time.ctime() + " -----")
    printLog(fileName, Border)
    printLog(fileName, "-------- Top 10 memory consuming processes -------")
    printLog(fileName, Border)
    printLog(fileName, "------------------ System Report -----------------")

    Data = processScan3()
    count = 0

    for info in Data:
        
        if info.get("rss") != "Access Denied":
            rss_MB = info["rss"] / (1024*1024)
        else:
            rss_MB = "Access Denied"

        if info.get("vms") != "Access Denied":
            vms_MB = info["vms"] / (1024*1024)
        else:
            vms_MB = "Access Denied"

        printLog(fileName, "PID : %s" % info.get("pid"))
        printLog(fileName, "Name : %s" % info.get("name"))
        printLog(fileName, "Resident Set Size - actual RAM used : %s MB" % rss_MB)
        printLog(fileName, "Virtual Memory : %s MB" % vms_MB)
        # printLog(fileName, "Resident Set Size - actual RAM used : %s" % info.get("rss"))
        # printLog(fileName, "Virtual Memory : %s" % info.get("vms"))
        printLog(fileName, "Memory Percent : %s" % info.get("memory_percent"))
        printLog(fileName, "Timestamp : %s" % info.get("timestamp"))
        printLog(fileName, Border)
        count += 1

    printLog(fileName, "Total Number of Processes : " + str(count))
    printLog(fileName, Border)
    printLog(fileName, "------------------ End of Report -----------------")
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
            createMemoryLog(fileName)

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