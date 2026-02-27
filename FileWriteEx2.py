#Program for Demonstrating How to write the Data to the File
#FileWriteEx2.py
while(True):
    print("-"*50)
    sno=input("Enter Student Number:")
    sname=input("Enter Student Name:")
    marks=float(input("Enter Student Marks:"))
    #Here sno,sname,marks are Called Objects and resides in Main Memory
    with open("student.data","a") as fp:
        fp.write(str(sno)+"\t")
        fp.write(sname+"\t")
        fp.write(str(marks)+"\n")
        print("Student Data Saved in File")
    ch=input("Do you want to Insert Another Record(yes/no):")
    if ch.lower()=="no":
        print("Thx for Using this Program")
        break