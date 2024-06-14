import os
import shutil
import datetime
import schedule
import time


source_dir = input("Please select a folder you would like to backup: ")
destination_dir = input("Please select a folder where you would like to have your backup: ")

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"folder already exist in: {dest}")

copy_folder_to_directory(source_dir, destination_dir)

