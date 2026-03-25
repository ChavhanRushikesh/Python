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
Add Periodic Email Reporting Feature:-
    Automatically send system report through email at regular intervals.    
    Email must contain:-
        Log file attachment
        Summary of:
            Total processes
            Top CPU usage processes
            Top Memory usage processes
            Top Thread count processes
            Top Open file processes
Usage:- 
PlatformSurveillance.py "MarvellousLogs" "receiver@gmail.com" 10
    Where:
        MarvellousLogs→ log folder
        receiver@gmail.com receiver mail
        10 interval in minutes
"""
import sys
import time
import smtplib
from email.message import EmailMessage
from automationModule import *

# -------------------- Send email function --------------------
def send_email(log_file, receiver_email, sender_email="chavhanrushikesh23@gmail.com", password="ysqp eujc vfni ekqs"):
    try:
        msg = EmailMessage()
        msg["Subject"] = "System Monitoring Report"
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg.set_content("Please find attached the latest system monitoring report.\n\nSummary included in attachment.")

        # Attach the log file
        with open(log_file, "rb") as f:
            file_data = f.read()
            file_name = log_file.split("/")[-1]

        msg.add_attachment(file_data, maintype="text", subtype="plain", filename=file_name)

        # Connect and send email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender_email, password)
            smtp.send_message(msg)

        print(f"Email sent to {receiver_email} successfully.")

    except Exception as e:
        print("Error sending email:", e)

# -------------------- Generate all reports --------------------
def createSystemLogs(folderName):
    log_file = createLogFile(folderName)
    Border = "-" * 50

    # Memory Log
    DataMem = processScan3()
    printLog(log_file, Border)
    printLog(log_file, "Memory Usage Report")
    printLog(log_file, f"Log created: {time.ctime()}")
    printLog(log_file, Border)

    for p in DataMem:
        rss_MB = p["rss"]/1024/1024 if p["rss"]!="Access Denied" else "Access Denied"
        vms_MB = p["vms"]/1024/1024 if p["vms"]!="Access Denied" else "Access Denied"

        printLog(log_file, f"PID: {p['pid']}, Name: {p['name']}")
        printLog(log_file, f"RSS(MB): {rss_MB if rss_MB=='Access Denied' else f'{rss_MB:.2f}'}, VMS(MB): {vms_MB if vms_MB=='Access Denied' else f'{vms_MB:.2f}'}")
        printLog(log_file, f"Memory Percent: {p['memory_percent']}, Timestamp: {p['timestamp']}")
        printLog(log_file, Border)

    # CPU Log
    DataCPU = processScan4()
    printLog(log_file, "Top 10 CPU Consuming Processes")
    for p in DataCPU:
        printLog(log_file, f"PID: {p['pid']}, Name: {p['name']}, CPU%: {p['cpu_percent']}, Timestamp: {p['timestamp']}")
    printLog(log_file, Border)

    # Threads Log
    DataThread = processScan1()
    DataThread.sort(key=lambda x: x.get("num_threads",0), reverse=True)
    topThreads = DataThread[:10]
    printLog(log_file, "Top 10 Thread Count Processes")
    for p in topThreads:
        printLog(log_file, f"PID: {p['pid']}, Name: {p['name']}, Threads: {p['num_threads']}, Timestamp: {p['timestamp']}")
    printLog(log_file, Border)

    # Open Files Log
    DataFiles = processScan2()
    DataFiles.sort(key=lambda x: x.get("open_files",0) if isinstance(x.get("open_files",0), int) else 0, reverse=True)
    topFiles = DataFiles[:10]
    printLog(log_file, "Top 10 Open File Descriptor Processes")
    for p in topFiles:
        printLog(log_file, f"PID: {p['pid']}, Name: {p['name']}, Open Files: {p['open_files']}, Timestamp: {p['timestamp']}")
    printLog(log_file, Border)

    return log_file

# -------------------- Main Function --------------------
def main():
    if len(sys.argv) != 4:
        print("Usage: PlatformSurveillance.py <LogFolder> <ReceiverEmail> <IntervalInMinutes>")
        return

    folderName = sys.argv[1]
    receiver_email = sys.argv[2]
    interval = int(sys.argv[3])

    sender_email = "chavhanrushikesh19@gmail.com"   # replace with sender email
    password = "ysqp eujc vfni ekqs"                # replace with sender password or app password

    while True:
        try:
            log_file = createSystemLogs(folderName)
            send_email(log_file, receiver_email, sender_email, password)
            print(f"Next report in {interval} minutes...\n")
            time.sleep(interval*60)

        except KeyboardInterrupt:
            print("Monitoring stopped by user.")
            break

        except Exception as e:
            print("Error:", e)
            time.sleep(interval*60)

if __name__ == "__main__":
    main()
