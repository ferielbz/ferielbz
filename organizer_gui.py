import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Archives": [".zip", ".rar"]
}

def organize_files(folder):
    if not folder:
        messagebox.showwarning("No Folder", "Please select a folder first.")
        return

    count = 0
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        if os.path.isfile(filepath):
            ext = os.path.splitext(filename)[1].lower()
            for folder_name, extensions in file_types.items():
                if ext in extensions:
                    target_folder = os.path.join(folder, folder_name)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(filepath, os.path.join(target_folder, filename))
                    count += 1
                    break

    messagebox.showinfo("Done", f"Organized {count} files successfully!")

def browse_folder():
    folder = filedialog.askdirectory()
    folder_path.set(folder)

def run_organizer():
    organize_files(folder_path.get())

# GUI Setup
root = tk.Tk()
root.title("Auto Folder Organizer")
root.geometry("400x200")
root.resizable(False, False)

folder_path = tk.StringVar()

tk.Label(root, text="Select a folder to organize:", font=("Arial", 12)).pack(pady=10)
tk.Entry(root, textvariable=folder_path, width=40).pack()
tk.Button(root, text="Browse", command=browse_folder).pack(pady=5)
tk.Button(root, text="Organize Files", command=run_organizer, bg="green", fg="white").pack(pady=10)

root.mainloop()
