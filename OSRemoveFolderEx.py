#Program for Removing the Folder--rmdir() of os module
#OSRemoveFolderEx.py
import os
try:
    os.rmdir("APS")
    print("Folder Removed")
except FileNotFoundError:
    print("Folder Not Existing")
except OSError:
    print("Ensure that Folder Must be Empty")