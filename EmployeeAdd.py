#EmployeeAdd.py<--File Name and Module Name
import pickle,sys
sys.path.append("C:\\Users\\shiva\\PycharmProjects\\Exceptions")
from NameValidation import validate
from NameExcept import InvalidNameError, EmptyNameError, SpaceError
def addemployee():
    with open("C:\\Users\\shiva\\PycharmProjects\\files\\empproject.data","ab") as fp:
        try:
            #accept the emp values from Key Board
            print("-"*50)
            empno=int(input("\tEnter Employee Number:"))
            empname=validate(input("\tEnter Employee Name:"))
            empsal=float(input("\tEnter Employee Salary:"))
            empcompname=validate(input("\tEnter Employee Company Name:"))
            print("-" * 50)
            #Create an Object of List
            lst=list()
            #add the employee values to list object
            lst.append(empno)
            lst.append(empname)
            lst.append(empsal)
            lst.append(empcompname)
            #save list object into the file of secondary memory
            pickle.dump(lst,fp)
            print("Employee Data saved Successfully in to the file")
            print("-" * 50)
        except ValueError:
            print("\tDON'T ENTER ALNUMS,STRS AND SYMBOLS FOR ENO,SALARY")
        except InvalidNameError:
            print("\tInvalid Name / Comp Name-try again")
        except EmptyNameError:
            print("\tU Must Enter Name/ Comp Name-try again")
        except SpaceError:
            print("\tDon't Enter Space for Ur Name-try again")
