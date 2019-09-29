# Python Program - List All Files in Directory

import glob, os

os.chdir(f"C:\Users\Mukund\Downloads")
for file in glob.glob("*.*"):
    print(file)