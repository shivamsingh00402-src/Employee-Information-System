#FileOpenEx3.py
try:
    with open("stud1.data","r") as fp:
        print("-------------------------------------------")
        print("File opened successfully in Read Mode")
        print("Type of tp=", type(fp))
        print("\tIs File Closed within with open() as:", fp.closed)
        print("-------------------------------------------")
    print("\nIs File Closed after with open() as:", fp.closed)
except FileNotFoundError:
    print("File Not Found")
finally:
    try:
        print("Is File Closed finally:", fp.closed)
    except NameError:
        print("File Name Not Yet Opened-No need to Close")
