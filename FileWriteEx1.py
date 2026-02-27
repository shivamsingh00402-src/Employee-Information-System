#Program for Demonstrating How to write the Data to the file
#FileWriteEx1.py
sno=400
sname="Dennis"
marks=94.56
#Here sno,sname,marks,are called objects and resides in Main Memory
with open("student.data","a") as fp:
    fp.write(str(sno)+"\t")
    fp.write(sname+"\t")
    fp.write(str(marks)+"\t")
    print("Student data Saved in File")