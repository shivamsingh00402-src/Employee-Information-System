#EmployeeUpdate.py<----File Name and Module Name
import pickle
def updateemployee():
    # Code for Getting the records from file
    records = []  # Outer List for Holding the Records of File
    with open("C:\\Users\\shiva\\PycharmProjects\\files\\empproject.data","rb") as fp:
        while (True):
            try:
                record = pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    #Get the employee Number to Update
    found = False
    empno = int(input("\tEnter Employee Number to Update:"))
    for recordindex in range(len(records)):
       if(records[recordindex][0]==empno):
           recno=recordindex
           found=True
           break
    if(found):
        empsal=float(input("\tEnter Employee New Salary:"))
        empcompname=input("\tEnter Employee New Comp Name:")
        records[recno][2]=empsal
        records[recno][3]=empcompname
        with open("C:\\Users\\shiva\\PycharmProjects\\files\\empproject.data","wb") as fp:
            for record in records:
                pickle.dump(record, fp)
        print("\tEmployee Data Updated--verify")
    else:
        print("\tEmployee Number Not Found")
