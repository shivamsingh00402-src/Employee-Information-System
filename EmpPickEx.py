#Program for Reading employee Values from Key Board and save them in File by using Pickling Process.
#EmpPickEx.py
import pickle
def saveempdata():
    with open("emp.pick","ab") as fp:
        while True:
            #Accepting the emp values from KeyBoard
            print("-"*50)
            empno=int(input("Enter Employee Number: "))
            empname=input("Enter Employee Name: ")
            empsal=input("Enter Employee Salary: ")
            empcompname=input("Enter Employee Company Name: ")
            print("-"*50)
            #Create an Object of List
            lst=list()
            #add the employee values to list object
            lst.append(empno)
            lst.append(empname)
            lst.append(empsal)
            lst.append(empcompname)
            #Save list object into the file of secondary memory
            pickle.dump(lst,fp)
            print("Employee Data saved Successfully in to the file")
            print("-"*50)
            ch=input("Do you want to Insert Another Record(yes/no):")
            if ch.lower()=="no":
                print("Thx for Using Program👍")
                break

#Main Program
saveempdata()