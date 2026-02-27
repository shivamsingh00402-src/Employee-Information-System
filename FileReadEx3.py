#Program of Reading the content of any File By accepting the File Name
#from KeyBoard
#FileReadEx3.py
from FileReadEx2 import filedata
def displayFileContent():
    try:
        filename=input("Enter Any File Name:")
        with open(filename,"r") as fp:
            filedata=fp.read()
            print(filedata)
    except FileNotFoundError:
        print("File Does Not Exist")

#Main Program
displayFileContent()