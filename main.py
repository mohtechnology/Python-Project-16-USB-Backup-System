import os
import shutil
import time

# Function to detect USB drives on Windows
def get_drives():
    drives = []
    bitmask = os.popen('wmic logicaldisk get name').read()
    for drive in bitmask.split('\n'):
        if drive.strip() and "Name" not in drive:
            drives.append(drive.strip())
    return drives

# Function to copy files from source to destination
def copy_files(src, dest):
    if not os.path.exists(dest):
        os.makedirs(dest)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dest, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, False, None)
        else:
            shutil.copy2(s, d)

# Specify the folder where you want to copy files
destination_folder = "C:/Users/mohsh/Documents/USB_Backup"

# Store the initial drives to detect new ones
initial_drives = get_drives()

print("Waiting for USB drive to be inserted...")

while True:
    current_drives = get_drives()
    
    # Check if a new drive is detected
    new_drives = list(set(current_drives) - set(initial_drives))
    
    if new_drives:
        print(f"USB drive detected: {new_drives[0]}")
        usb_drive = new_drives[0]  # Assuming only one USB drive is inserted
        
        # Copy contents from USB to the destination folder
        copy_files(usb_drive, destination_folder)
        print(f"All files copied from {usb_drive} to {destination_folder}")
        
        break
    
    time.sleep(2)  # Check every 2 seconds
