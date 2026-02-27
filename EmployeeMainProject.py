#EmployeeMainProject.py
from EmpMenu import menu
from EmployeeAdd import addemployee
from EmployeeSearch import searchemployee
from EmployeeView import viewallemployee, viewemployee
from EmployeeUpdate import updateemployee
from EmployeeDelete import deleteemployee
while(True):
    try:
        menu()
        ch=int(input("Enter your choice: "))
        match(ch):
            case 1:
                addemployee()
            case 2:
                 deleteemployee()
            case 3:
                updateemployee()
            case 4:
                viewemployee()
            case 5:
                viewallemployee()
            case 6:
                searchemployee()
            case 7:
                print("\tTHX FOR USING THIS PROJECT👍")
                break
            case _:
                print("\tUR Selection of Choice is Wrong-try again")
    except ValueError:
        print("\tDon't enter alnums,atrs and symbols for Choice--try again")
