#EmployeeSearch.py<--File Name and Module Name
import pickle
def searchemployee():
    # Code for Getting the records from file
    records = []  # Outer List for Holding the Records of File
    with open("C:\\Users\\shiva\\PycharmProjects\\files\\empproject.data","rb") as fp:
        while (True):
            try:
                record = pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    #Get the employee to search
    found=False
    empno = int(input("\tEnter Employee Number to view Details:"))
    for record in records:
        if(record[0]==empno):
            found=True
            break
    if(found):
        print("\tEmployee is Valid")
    else:
        print("\tEmployee Does not Exist")
