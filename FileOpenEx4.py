#FileOpenEx4.py
try:
    with open("stud.data","r+") as fp:
        print("---------------------------------------------")
        print("\tFile opened successfully in Read Mode")
        print("\t Type of tp=",type(fp))
        print("\t Is File Closed within with open() as:",fp.closed)
        print("------------------------------------------------")
        print("\tName of the File=",fp.name)
        print("\t File Mode=",fp.mode)
        print("\tIs File Readable=",fp.readable())
        print("\tIs File Writable=",fp.writable())
        print("----------------------------------------")
    print("\n Is File Closed after with open() as:",fp.closed)
except FileNotFoundError:
    print("File Not Found Error")