#Program for Creating a Folder---mkdir() of os module
#OSFolderCreateEx.py
import os
try:
    os.mkdir("APS")
    print("Folder Created")
except FileExistsError:
    print("Folder Already Exists")
except FileNotFoundError:
    print("Root Folder Does Not Exist")