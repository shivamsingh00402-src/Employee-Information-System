#EmployeeDelete.py<-----------File Name and Module Name
import pickle
def deleteemployee():
    #Code For Getting the records from file
    records=[] #Outer List for Holding the Records of File
    with open("C:\\Users\\shiva\\PycharmProjects\\files\\empproject.data","rb") as fp:
        while True:
            try:
                record = pickle.load(fp)
                records.append(record)
            except EOFError:
                break
        #Accept the employee Number for deleting the record
        empno=int(input("Enter Employee Number to Delete: "))
        found = False
        for recindex in range(0,len(records)):
            if (records[recindex][0]==empno):
                recno=recindex
                found = True
                break
        if found:
            records.pop(recno) # OR records.remove(records[recno])
            #Save the remaining records
            with open("C:\\Users\\shiva\\PycharmProjects\\files\\empproject.data","wb")as fp:
                for record in records:
                    pickle.dump(record,fp)
                print("\tEmployee Data Deleted--verify")
        else:
            print("\t Employee Number Does Not Exist")