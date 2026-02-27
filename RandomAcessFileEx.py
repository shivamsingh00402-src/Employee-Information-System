#Program for Demonstrating the Need of Random Access Files.
#FilePointerObj.tell()--->Gives the Index of Data where File Pointer Points
#FilePointer.seek(index)--->Will Reset the File Pointer to the Specified Index
#RandomAcessFileEx.py
with open("hyd.info","r") as fp:
    print("Initially fp Points to:",fp.tell())
    filedata = fp.read(5)
    print("File Data=",filedata) # Pytho
    print("Now fp Points to:",fp.tell()) # 5
    print("-------------------------------------------")
    filedata = fp.read(5)
    print("File Data=",filedata)  # n is
    print("Now fp Points to:",fp.tell()) #10
    print("-------------------------------------------")
    filedata = fp.read(6)
    print("File Data=",filedata) # an OOPS
    print("Now fp Points to:",fp.tell()) # 16
    print("-------------------------------------------")
    filedata = fp.read()
    print("File Data=",filedata)
    print("Now fp Points to:",fp.tell()) # 88
    print("-------------------------------------------")
