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
Logging System:
    Create a Logs/ folder
    Backup start time
    Files copied
    Zip file name
    Errors (if any)
"""
import sys
import time
import schedule

from MarvellousMod import setup_logger, log_info, log_error, backup_files, create_zip

def MarvellousDataShieldStart(source):
    try:
        Border = "-" * 50
        BackupName = "MarvellousBackup"

        log_info(Border)
        log_info(f"Backup process started at: {time.ctime()}")
        log_info(Border)

        files = backup_files(source, BackupName)
        zip_file = create_zip(BackupName)

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
            option = sys.argv[1].lower()
            if option == "--h":
                log_info("This script is used to :")
                log_info("1 : Takes Auto backup at given time")
                log_info("2 : Backup only new and updated files")
                log_info("3 : Create an archive of the backup periodically")

            elif option == "--u":
                log_info("Use the automation script as :")
                log_info("ScriptName.py TimeInterval SourceDirectory")
                log_info("TimeInterval : Time in minutes for periodic scheduling")
                log_info("SourceDirectory : Name of Directory to backup")

            else:
                log_error("Invalid option provided. Use --h or --u for help")

        elif len(sys.argv) == 3:
            interval = sys.argv[1]
            source = sys.argv[2]

            log_info(f"Inside project logic. Time Interval: {interval} minutes, Directory: {source}")
            schedule.every(int(interval)).minutes.do(MarvellousDataShieldStart, source)

            log_info(Border)
            log_info("Data Shield system started successfully")
            log_info(f"TimeInterval in minutes: {interval}")
            log_info("Press Ctrl + C to stop the execution")
            log_info(Border)

            while True:
                schedule.run_pending()
                time.sleep(1)

        else:
            log_error("Invalid number of command line arguments. Use --h or --u for help")

    except Exception as e:
        log_error(f"Main execution error: {e}")

    log_info(Border)
    log_info("--------- Thank you for using our script ---------")
    log_info(Border)

if __name__ == "__main__":
    main()