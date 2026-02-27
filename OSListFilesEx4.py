#Program for Listing the Files in a Folder---listdir() of os module
#OSListFilesEx4.py
import os
FilesList=os.listdir("C:\\Users\\shiva\\PycharmProjects\\files")
print("Number of Files=",len(FilesList))
print("-"*50)
nop=0
for filename in FilesList:
    if ".py" in filename:
        print(filename)
        nop=nop+1
print("-"*50)
print("Number of Python Files=",nop)
print("-"*50)