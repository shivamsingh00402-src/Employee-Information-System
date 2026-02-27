#Program for Reading the Data from KeyBoard and Write It to the file
#DynamicWriteEx.py
print("Enter the Data to File and Press @ to stop:")
with open("hyd.info","a") as fp:
    while (True):
        kbddata = input()
        if kbddata != "@":
            fp.write(kbddata + "\n")
        else:
            print("Data Written to the File")
            break
