#Program for Removing the file name--remove() of os module
#OSRemoveFileEx.py
import os
try:
    os.remove("C:\\Users\\shiva\\PycharmProjects\\files\\APS\\FactEx.py")
    print("File Name removed")
except FileNotFoundError:
    print("File Name not found")