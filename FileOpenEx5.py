#FileOpenEx5.py
with open("stud3.data","a+") as fp:
    print("-------------------------------------------")
    print("\tFile Created opened successfully in Write Mode")
    print("\tType of tp=", type(fp))
    print("\tIs File Closed within with open() as:", fp.closed)
    print("-------------------------------------------")
    print("\tName of the File=",fp.name)
    print("\tFile Mode=",fp.mode)
    print("\tIs File Readable=",fp.readable())
    print("\tIs File Writable=",fp.writable())
    print("-------------------------------------------")