# Program for Reading the Records from File (emp.pick)
#EmpUnPickEx.py
import pickle
def readrecords():
    try:
        print("-"*50)
        with open("emp.pick","rb") as fp:
            while(True):
                try:
                    record = pickle.load(fp)
                    for val in record:
                        print("\t {}".format(val),end="\t")
                        print()
                except EOFError:
                    print("-"*50)
                    break
    except FileNotFoundError:
        print("File Does Not Exist")


#Main Program
readrecords()
