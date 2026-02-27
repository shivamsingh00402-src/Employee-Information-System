# Program for Reading the Data from File
#FileReadEx1.py
try:
    with open("student.data","r") as fp:
        filedata=fp.read()
        print(filedata,type(filedata))
except FileNotFoundError:
    print("File Does Not Exist")