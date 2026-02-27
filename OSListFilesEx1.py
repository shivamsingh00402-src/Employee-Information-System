#Program for Listing the Files in a Folder---listdir() of os module
#OSListFilesEx1.py
import os
FileList = os.listdir("C:\\Users\\shiva\\PycharmProjects\\files\\")
print("Number of Files=",len(FileList))
print("-"*50)
for filename in FileList:
    print("\t{}".format(filename))
    print("-"*50)