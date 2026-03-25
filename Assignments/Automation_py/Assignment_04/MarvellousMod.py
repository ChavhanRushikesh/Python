#----------------------------------------------------------------------------------
# 1. Logging
# 2. Hash calculation
# 3. Backup
# 4. Zip creation
#----------------------------------------------------------------------------------

import os
import logging
import hashlib
import shutil
import sys
import zipfile
import time
import smtplib
import csv
from email.message import EmailMessage

LOG_DIR = "Logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOG_FILE = os.path.join(LOG_DIR, f"MarvellousDataShield_{time.strftime('%Y-%m-%d')}.log")

def setup_logger():
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
def get_log_file_path():
    return LOG_FILE

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)

def calculate_hash(path):
    try:
        hobj = hashlib.md5()
        with open(path, "rb") as fobj:
            while True:
                data = fobj.read(1024)
                if not data:
                    break
                hobj.update(data)
        return hobj.hexdigest()
    except Exception as e:
        log_error(f"Error calculating hash for {path}: {e}")
        raise

def backup_files(source, destination, ignore_ext):
    copied_files = []
    try:
        if not os.path.exists(source) or not os.path.isdir(source):
            raise Exception(f"Invalid source directory: {source}")

        os.makedirs(destination, exist_ok=True)
        log_info("Backup folder prepared")

        for root, dirs, files in os.walk(source):
            for file in files:
                ext = os.path.splitext(file)[1].lower()

                if ext in ignore_ext:
                    log_info(f"Ignored file: {file}")
                    continue

                src_path = os.path.join(root, file)
                relative = os.path.relpath(src_path, source)
                dest_path = os.path.join(destination, relative)
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)

                # Copy only new or updated files
                if (not os.path.exists(dest_path)) or (calculate_hash(src_path) != calculate_hash(dest_path)):
                    shutil.copy2(src_path, dest_path)
                    copied_files.append(relative)

        log_info(f"Files copied: {len(copied_files)}")
        return copied_files

    except Exception as e:
        log_error(f"Backup error: {e}")
        raise

def create_zip(folder):
    try:
        if not os.path.exists(folder) or not os.path.isdir(folder):
            raise Exception(f"Invalid folder for zipping: {folder}")

        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        zip_name = f"{folder}_{timestamp}.zip"

        with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zobj:
            for root, dirs, files in os.walk(folder):
                for file in files:
                    full_path = os.path.join(root, file)
                    relative = os.path.relpath(full_path, folder)
                    zobj.write(full_path, relative)

        log_info(f"Zip file created: {zip_name}")
        return zip_name

    except Exception as e:
        log_error(f"Zip creation error: {e}")
        raise

def send_backup_email(zip_path,receiver_email):
    try:
        sender_email = "chavhanrushikesh19@gmail.com"
        sender_password = "dnfj sfff ssdf dfef"

        zip_filename = os.path.basename(zip_path)
        log_path = get_log_file_path()

        msg = EmailMessage()
        msg['Subject'] = f'Backup Completed: {zip_filename}'
        msg['From'] = sender_email
        msg['To'] = receiver_email

        msg.set_content(f"""
hlw sir,
    Rushikesh here, I have completed the backup process and send you the email notification as well.
    the backup file is attached with this email.also attached log file for your reference.
    Please find the details below:
                        
    Backup File: {zip_filename}

    Attached:
    - ZIP file
    - Log file
""")

        with open(zip_path, 'rb') as f:
            msg.add_attachment(
                f.read(),
                maintype='application',
                subtype='zip',
                filename=zip_filename
            )

        with open(log_path, 'rb') as f:
            msg.add_attachment(
                f.read(),
                maintype='text',
                subtype='plain',
                filename=os.path.basename(log_path)
            )

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)

        log_info("Email notification sent successfully")

    except Exception as e:
        log_error(f"Email sending failed: {e}")
        raise

def restore_backup(zip_file, destination):
    try:
        if not os.path.exists(zip_file):
            raise Exception(f"Zip file does not exist: {zip_file}")

        if not zipfile.is_zipfile(zip_file):
            raise Exception(f"Invalid zip file: {zip_file}")

        if not os.path.exists(destination):
            os.makedirs(destination)

        log_info(f"Restore started from {zip_file}")
        log_info(f"Destination directory: {destination}")

        with zipfile.ZipFile(zip_file, 'r') as zobj:
            zobj.extractall(destination)

        log_info("Restore completed successfully")

    except Exception as e:
        log_error(f"Restore failed: {e}")
        raise

def ignore_ext(ext_file=None):
    default_ext = {".tmp", ".log", ".exe"}
    final_ext = set(default_ext)

    try:
        # Always start with default extensions
        log_info(f"Default extensions to ignore: {default_ext}")
        
        if ext_file:
            if not os.path.exists(ext_file):
                raise Exception(f"Extension file not found: {ext_file}")

            if not os.path.isfile(ext_file):
                raise Exception("Provided extension input is not a file")

            user_ext = set()
            with open(ext_file, "r") as f:
                for line in f:
                    ext = line.strip().lower()

                    if not ext:
                        continue

                    if not ext.startswith("."):
                        log_error(f"Invalid extension format ignored: {ext}")
                        continue

                    user_ext.add(ext)
                    final_ext.add(ext)

            log_info(f"User defined extensions loaded from {ext_file}: {user_ext}")
        else:
            log_info("No user extension file provided. Using default ignore list only.")

        log_info(f"Total extensions to ignore (Default + User-defined): {final_ext}")
        return final_ext

    except Exception as e:
        log_error(f"Error preparing ignore extensions: {e}")
        log_info(f"Falling back to default extensions only: {default_ext}")
        return default_ext

def save_backup_history(zip_file, num_files):
    """Save backup history to CSV file with date, number of files, and zip size"""
    history_file = "BackupHistory.csv"
    
    try:
        if not os.path.exists(zip_file):
            raise Exception(f"Zip file not found: {zip_file}")
        
        # Get zip file size in MB
        zip_size_bytes = os.path.getsize(zip_file)
        zip_size_mb = round(zip_size_bytes / (1024 * 1024), 2)
        
        # Get backup date and time
        backup_date = time.strftime("%Y-%m-%d %H:%M:%S")
        zip_filename = os.path.basename(zip_file)
        
        # Check if file exists to write header or not
        file_exists = os.path.exists(history_file)
        
        with open(history_file, "a", newline="") as f:
            writer = csv.writer(f)
            
            # Write header if file is new
            if not file_exists:
                writer.writerow(["Date", "Number of Files", "Zip Size (MB)", "Zip Filename"])
                log_info("Backup history file created")
            
            # Write backup entry
            writer.writerow([backup_date, num_files, zip_size_mb, zip_filename])
            log_info(f"Backup history saved: {backup_date}, Files: {num_files}, Size: {zip_size_mb} MB")
    
    except Exception as e:
        log_error(f"Error saving backup history: {e}")

def display_backup_history():
    """Display all backup history from CSV file"""
    history_file = "BackupHistory.csv"
    
    try:
        if not os.path.exists(history_file):
            print("No backup history found. Run backup first.")
            log_info("Backup history file does not exist")
            return
        
        print("\n" + "=" * 80)
        print("                         BACKUP HISTORY TRACKER")
        print("=" * 80)
        
        with open(history_file, "r") as f:
            reader = csv.reader(f)
            rows = list(reader)
            
            if not rows:
                print("No backup history available")
                log_info("Backup history file is empty")
                return
            
            # Print header
            header = rows[0]
            print(f"{header[0]:<20} {header[1]:<20} {header[2]:<15} {header[3]:<30}")
            print("-" * 80)
            
            # Print each row
            for row in rows[1:]:
                print(f"{row[0]:<20} {row[1]:<20} {row[2]:<15} {row[3]:<30}")
            
            print("=" * 80)
            log_info(f"Displayed backup history ({len(rows)-1} backups)")
    
    except Exception as e:
        log_error(f"Error displaying backup history: {e}")
        print(f"Error reading backup history: {e}")