#----------------------------------------------------------------------------------
# Please follow below rules while designing automation script as
#   * Accept input through command line or through file.
#   * Display any message in log file instead of console.
#   * For separate task define separate function.
#   * For robustness handle every expected exception.
#   * Perform validations before taking any action.
#   * Create user defined modules to e functionality,
# Please add below features in our project named as Marvellous Data Shield System
#----------------------------------------------------------------------------------
"""
Restore Feature
Add a command:
    python Script.py --restore zipFileName.zip DestinationDirectory
    Extract backup to given directory
"""
import sys
import time
import schedule

from MarvellousMod import (
    restore_backup,
    setup_logger,
    log_info,
    log_error,
    backup_files,
    create_zip,
    send_backup_email
)

def MarvellousDataShieldStart(data):
    if len(sys.argv) > 3 :
        receiver_email = sys.argv[3]
    else:
        receiver_email = "rushikeshchavhan23@gmail.com"

    try:
        Border = "-" * 50
        BackupName = "MarvellousBackup"

        log_info(Border)
        log_info(f"Backup process started at: {time.ctime()}")
        log_info(Border)

        files = backup_files(data, BackupName)
        zip_file = create_zip(BackupName)
        send_backup_email(zip_file,receiver_email)
        
        log_info(Border)
        log_info("Backup completed successfully")
        log_info(f"Files copied: {len(files)}")
        log_info(f"Zip file created: {zip_file}")
        log_info(Border)

    except Exception as e:
        log_error(f"Backup process failed: {e}")

def main():
    setup_logger()
    Border = "-" * 50
    log_info(Border)
    log_info("----- Marvellous Data Shield system -----")
    log_info(Border)

    try:
        if len(sys.argv) == 2:
            arvar = sys.argv[1]
            if arvar == "--h" or arvar == "--H":
                log_info("This script is used to :")
                log_info("1 : Takes Auto backup at given time")
                log_info("2 : Backup only new and updated files")
                log_info("3 : Create an archive of the backup periodically")
                log_info("4 : Send backup archive to email periodically")
                log_info("5 : Restore backup from archive (under development)")

            elif arvar == "--u" or arvar == "--U":
                log_info("Use the automation script as :")
                log_info("ScriptName.py TimeInterval SourceDirectory")
                log_info("TimeInterval : Time in minutes for periodic scheduling")
                log_info("SourceDirectory : Name of Directory to backup")
                log_info("Example : python Script.py 1 Data")
                log_info("Restore file of backup")

            else:
                log_error("Invalid option provided. Use --h or --u for help")
                print("Invalid option provided. Use --h or --u for help")

        #python Program.py 1 Data receiveremail@gmail.com
        elif len(sys.argv) == 3:
            timeObj = sys.argv[1]
            data = sys.argv[2]

            log_info(f"Inside project logic. Time Interval: {timeObj} minutes, Directory: {data}")
            schedule.every(int(timeObj)).minutes.do(MarvellousDataShieldStart, data)

            log_info(Border)
            log_info("Data Shield system started successfully")
            log_info(f"TimeInterval in minutes: {timeObj}")
            log_info("Press Ctrl + C to stop the execution")
            log_info(Border)

            while True:
                schedule.run_pending()
                time.sleep(1)

       # python Script.py --restore zipFileName.zip DestinationDirectory
        elif len(sys.argv) == 4 and sys.argv[1].lower() == "--restore":
            zipName = sys.argv[2]
            destination = sys.argv[3]
            restore_backup(zipName,destination)
            log_info("Restore process completed successfully")

        else:
            log_error("Invalid number of command line arguments. Use --h or --u for help")
            print("Invalid number of command line arguments. Use --h or --u for help")

    except Exception as e:
        log_error(f"Main execution error: {e}")

    log_info(Border)
    log_info("--------- Thank you for using our script ---------")
    log_info(Border)

if __name__ == "__main__":
    main()