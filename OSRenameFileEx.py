#Program for Renaming a File Name---rename() of os module
#OSRenameFileEx.py
import os
try:
    os.rename(dst="emp.pick",src="std.pick")
    print("File name Renamed")
except FileNotFoundError:
    print("Source File Name not Exist")