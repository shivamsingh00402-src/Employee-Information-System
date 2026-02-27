#EmployeeView.py<---File Name and Module Name
import pickle
def viewemployee():
    #Code for Getting the records from file
    records=[] # Outer List for Holding the Records of File
    with open("C:\\Users\\shiva\\PycharmProjects\\files\\empproject.data","rb") as fp:
        while(True):
            try:
                record = pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    #display the records
    found=False
    empno = int(input("\tEnter Employee Number to view Details:"))
    for record in records:
        if(record[0]==empno):
            found=True
            emprec=record
            break
    print("-"*50)
    if(found):
        print("\tEmployee Number={}".format(emprec[0]))
        print("\tEmployee Name={}".format(emprec[1]))
        print("\tEmployee Salary={}".format(emprec[2]))
        print("\tEmployee Company Name={}".format(emprec[3]))
    else:
        print("\tEmployee Number Does Not Exist")
    print("-" * 50)

def viewallemployee():
    try:
        print("-" * 50)
        print("\tENO\t\tNAME\tSAL\t\tCOMPNAME")
        print("-" * 50)
        with open("C:\\Users\\shiva\\PycharmProjects\\files\\empproject.data","rb") as fp:
            while(True):
                try:
                    record = pickle.load(fp)
                    for val in record:
                        print("\t{}".format(val),end="\t")
                    print()
                except EOFError:
                    print("-"*50)
                    break
    except FileNotFoundError:
        print("File Does Not Exist")
