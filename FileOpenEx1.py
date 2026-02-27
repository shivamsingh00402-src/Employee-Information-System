#program for Demonstrating How to Open the file Name
#FileOpenEx1.py
try:
    fp=open("stud.data","r")
except FileNotFoundError:
    print("File Does Not Exist")
else:
    print("File opened successfully in Read Mode")
    print("Type of tp=", type(fp))
finally:
    try:
        print("I am from finally Block")
        print("\tIs File Closed before close():", fp.closed)
        fp.close() # For Manual Closing
        print("\tIs File Closed after close():", fp.closed)
    except NameError:
        print("File Name Not Yet Opened-No need to Close")
