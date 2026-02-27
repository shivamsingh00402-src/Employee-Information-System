#Program for Listing the Files in a Folder---listdir() of os module
#OSListFilesEx2.py
import os
FileList = os.listdir("C:\\Users\\shiva\\PycharmProjects\\files")
print("Number of Files=",len(FileList))
print("-"*50)
nop=0
for filename in FileList:
    if filename.endswith(".py"):
        print(filename)
        nop=nop+1
print("-"*50)
print("Number of Python Files=",nop)
print("-"*50)