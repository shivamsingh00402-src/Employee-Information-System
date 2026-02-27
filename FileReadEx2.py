#Program for Reading the Data from File
#FileReadEx2.py
try:
    print("-"*50)
    with open("student.data","r") as fp:
        filedata =fp.readlines()
        for record in filedata:
            print(record)
        print("-"*50)
except FileNotFoundError:
    print("File Does Not Exist")
