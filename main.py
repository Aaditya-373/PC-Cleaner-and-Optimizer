import os
import shutil
import time
import subprocess


file_clear = input("(PC Cleaner will clear all temp files,temporary internet files,DirectX Shader Cache,Delivery optimization files,Downloaded Program Files,and finally clear the Recycle Bin:)\nIf you would like to clear your PC, type 'clear',otherwise type 'exit':\n")

if file_clear == 'clear':
    temp_directory = os.environ['TEMP']
    other_temp = os.environ['SystemRoot'] + '\\Temp'
    prefetch = os.environ['SystemRoot'] + '\\Prefetch'
 
    print("Clearing user temp files...")
    time.sleep(3)
    os.chdir(temp_directory)
    files = os.listdir()
    # print(files)
    for file in files:
        try:
            temp_file_path = os.path.join(temp_directory, file)
            if os.path.isfile(temp_file_path):
                os.remove(temp_file_path)
                print(f"Deleted file: {temp_file_path}")
            elif os.path.isdir(temp_file_path):
                shutil.rmtree(temp_file_path)
                print(f"Deleted folder:{temp_file_path}")

        except PermissionError as e:
            print(f"PermissionError: {e} - Skipped file: {file}")
            time.sleep(0.25)
    print()
    print()
    print("User temp files cleared.")
    print()
    print()
    print("Clearing Temp folder...")
    time.sleep(3)
    os.chdir(other_temp)
    files = os.listdir()
    for file in files:
        try:
            other_temp_file_path = os.path.join(other_temp, file)
            if os.path.isfile(other_temp_file_path):
                os.remove(other_temp_file_path)
                print(f"Deleted file: {other_temp_file_path}")
            elif os.path.isdir(other_temp_file_path):
                shutil.rmtree(other_temp_file_path)
                print(f"Deleted folder:{other_temp_file_path}")

        except PermissionError as e:
            print(f"PermissionError: {e} - Skipped file: {file}")
            time.sleep(1)
    print()
    print()
    print("Temp folder cleared.")
    print()
    print()
    print("Deleting prefetch files...")
    time.sleep(3)
    os.chdir(prefetch)
    files = os.listdir()
    for file in files:
        try:
            prefetch_file_path = os.path.join(prefetch, file)
            if os.path.isfile(prefetch_file_path):
                os.remove(prefetch_file_path)
                print(f"Deleted file: {prefetch_file_path}")
            elif os.path.isdir(prefetch_file_path):
                shutil.rmtree(prefetch_file_path)
                print(f"Deleted folder:{prefetch_file_path}")

        except PermissionError as e:
            print(f"PermissionError: {e} - Skipped file: {file}")
            time.sleep(1)
    print()
    print()
    print("Prefetch cleared.")
    print()
    print()
    print("To perform Disk Cleanup specifically,open the disk cleanup app and configure the desired settings,then run the script.\nOtherwise,run the script with default settings.\n")
    print("Performing Disk Cleanup...")
    time.sleep(3)
    # Run Disk Cleanup
    subprocess.run(['cleanmgr', '/sagerun:2'])
    print("Disk Cleanup Completed.\nExiting PC Cleaner...")
    time.sleep(2)
else:
    print("Exiting PC Cleaner...")


