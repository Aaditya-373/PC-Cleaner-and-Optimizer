import os
import shutil
import subprocess
from tkinter import messagebox
import customtkinter


def clear_temp_files():
    try:
        temp_directory = os.environ['TEMP']
        other_temp = os.environ['SystemRoot'] + '\\Temp'
        prefetch = os.environ['SystemRoot'] + '\\Prefetch'

        # Clear user temp files
        os.chdir(temp_directory)
        for file in os.listdir(temp_directory):
            try:
                temp_file_path = os.path.join(temp_directory, file)
                if os.path.isfile(temp_file_path):
                    os.remove(temp_file_path)
                elif os.path.isdir(temp_file_path):
                    shutil.rmtree(temp_file_path)
            except PermissionError as e:
                pass

        # Clear Temp folder
        os.chdir(other_temp)
        for file in os.listdir(other_temp):
            try:
                other_temp_file_path = os.path.join(other_temp, file)
                if os.path.isfile(other_temp_file_path):
                    os.remove(other_temp_file_path)
                elif os.path.isdir(other_temp_file_path):
                    shutil.rmtree(other_temp_file_path)
            except PermissionError as e:
                pass

        # Clear prefetch files
        os.chdir(prefetch)
        for file in os.listdir(prefetch):
            try:
                prefetch_file_path = os.path.join(prefetch, file)
                if os.path.isfile(prefetch_file_path):
                    os.remove(prefetch_file_path)
                elif os.path.isdir(prefetch_file_path):
                    shutil.rmtree(prefetch_file_path)
            except PermissionError as e:
                pass

        messagebox.showinfo("PC Cleaner", "Cleanup Completed")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def run_disk_cleanup():
    try:
        subprocess.run(['cleanmgr', '/sagerun:2'])
        messagebox.showinfo("PC Cleaner", "Disk Cleanup Completed")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def on_clear_button_click():
    result = messagebox.askyesno("PC Cleaner", "This will clear temp files and prefetch. Continue?")
    if result:
        clear_temp_files()


def on_cleanup_button_click():
    result = messagebox.askyesno("PC Cleaner", "This will run Disk Cleanup. Continue?")
    if result:
        run_disk_cleanup()


# Create the main application window
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
window = customtkinter.CTk()
window.configure(bg='#f0f0f0')
window.geometry("300x300")
window.title("PC Cleaner")

label = customtkinter.CTkLabel(window, text="PC CLEANER")
label.pack(padx=2.5)


frame = customtkinter.CTkFrame(master=window)
frame.pack(padx=20, pady=0.5,
           fill='x', expand=True)

title = customtkinter.CTkLabel(master=frame, text='PC Cleaner', fg_color="transparent")

# Create UI components
clear_button = customtkinter.CTkButton(master=frame, text="Clear Temp Files/Prefetch", command=on_clear_button_click)
cleanup_button = customtkinter.CTkButton(master=frame, text="Run Disk Cleanup", command=on_cleanup_button_click)
exit_button = customtkinter.CTkButton(master=frame, text="Exit", command=window.quit, fg_color="red")

# Layout UI components
clear_button.pack(pady=10)
cleanup_button.pack(pady=10)
exit_button.pack(pady=10)

# Start the main application loop
window.mainloop()
