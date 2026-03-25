# Automation Assignment 33 : Module

import os
import time
import psutil

# ------------------------------------------------------------
# Get timestamp for log file or process entry
# ------------------------------------------------------------
def get_timestamp():
    return time.strftime("%Y-%m-%d_%H-%M-%S")

# ------------------------------------------------------------
# Create log file and return full path
# ------------------------------------------------------------
def createLogFile(folderName):
    timestamp = get_timestamp()
    try:
        if not os.path.exists(folderName):
            os.mkdir(folderName)

        elif not os.path.isdir(folderName):
            return

        fileName = os.path.join(folderName,"Ass_Reports_%s.log" % timestamp)
        return fileName

    except Exception as e:
        return e

# ------------------------------------------------------------
# Write a single line to log file
# ------------------------------------------------------------
def printLog(fileName, report):
    try:
        with open(fileName, "a") as file:
            file.write(report + "\n")

    except Exception as e:
        return e

# ------------------------------------------------------------
# Scan processes for basic info (PID, name, threads)
# ------------------------------------------------------------
def processScan1():
    listProcess = []
    try:
        # Warm up CPU percent calculation
        for proc in psutil.process_iter():
            try:
                proc.cpu_percent()
            except Exception:
                pass

        time.sleep(0.2)

        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict(attrs=["pid", "name", "num_threads"])
                pinfo["timestamp"] = get_timestamp()
                listProcess.append(pinfo)
            except Exception:
                pass
    except Exception as e:
        return e

    return listProcess

# ------------------------------------------------------------
# Scan processes with open files
# ------------------------------------------------------------
def processScan2():
    listProcess = []
    try:
        # Warm up CPU percent calculation
        for proc in psutil.process_iter():
            try:
                proc.cpu_percent()
            except Exception:
                pass
        time.sleep(0.2)

        for proc in psutil.process_iter(["pid", "name", "num_threads"]):
            try:
                pinfo = proc.info.copy()  
                pinfo["open_files"] = proc.num_fds()
                pinfo["timestamp"] = get_timestamp()
            except (psutil.AccessDenied, psutil.NoSuchProcess):
                pinfo = proc.info.copy() 
                pinfo["open_files"] = "Access Denied"
                pinfo["timestamp"] = get_timestamp()

            listProcess.append(pinfo)

    except Exception as e:
        return e

    return listProcess

# ------------------------------------------------------------
# Scan processes and return top 10 memory consuming
# ------------------------------------------------------------
def processScan3():
    listProcess = []
    try:
         # Warm up CPU percent calculation
        for proc in psutil.process_iter():
            try:
                proc.cpu_percent()
            except Exception:
                pass

        time.sleep(0.2)
        for proc in psutil.process_iter(["pid", "name"]):
            try:
                pinfo = proc.info.copy()  
                mem_info = proc.memory_info()
                pinfo["rss"] = mem_info.rss
                pinfo["vms"] = mem_info.vms
                pinfo["memory_percent"] = proc.memory_percent()
                pinfo["timestamp"] = get_timestamp()

            except (psutil.AccessDenied, psutil.NoSuchProcess):
                pinfo = proc.info.copy() 
                pinfo["rss"] = "Access Denied"
                pinfo["vms"] = "Access Denied"
                pinfo["memory_percent"] = "Access Denied"
                pinfo["timestamp"] = get_timestamp()

            listProcess.append(pinfo)

        for p in listProcess:
            if p["memory_percent"] == "Access Denied":
                p["memory_percent_sort"] = 0
            else:
                p["memory_percent_sort"] = p["memory_percent"]

        listProcess.sort(key=lambda x: x["memory_percent_sort"], reverse=True)

        top10_processes = listProcess[:10]

        for p in top10_processes:
            del p["memory_percent_sort"]

        return top10_processes

    except Exception as e:
        return e
    
def processScan4():
    listProcess = []
    try:
        # Store all process objects
        processes = []
        for proc in psutil.process_iter(["pid", "name", "num_threads"]):
            processes.append(proc)

        # Warm up CPU counters
        for proc in processes:
            try:
                proc.cpu_percent(None)
            except Exception:
                pass

        time.sleep(1)

        # Get CPU usage
        for proc in processes:
            try:
                pinfo = proc.info.copy()
                pinfo["cpu_percent"] = proc.cpu_percent(None)
                pinfo["timestamp"] = get_timestamp()
            except (psutil.AccessDenied, psutil.NoSuchProcess):
                pinfo = proc.info.copy()
                pinfo["cpu_percent"] = "Access Denied"
                pinfo["timestamp"] = get_timestamp()

            listProcess.append(pinfo)

        for p in listProcess:
            if p["cpu_percent"] == "Access Denied":
                p["cpu_sort"] = 0
            else:
                p["cpu_sort"] = p["cpu_percent"]

        listProcess.sort(key=lambda x: x["cpu_sort"], reverse=True)

        top10 = listProcess[:10]

        for p in top10:
            del p["cpu_sort"]

        return top10

    except Exception as e:
        return e