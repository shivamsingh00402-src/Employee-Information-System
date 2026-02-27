#Program for Creating CSV File----writer() of csv module
#CSVFileCreateEx1.py--List in List
import csv #Step-1
colnames=["SNO","NAME","REMARKS"] #Step-2
records=[[100,"Vishnu","BEST"]
         [200,"Ramesh","Good"]
         [300,"Krishna","BEST"]
         [400,"RAVI","BETTER"]]  #Step-3
with open("C:\\Users\\shiva\\PycharmProjects\\CSV\\Notes\\studentdata.csv","w") as fp:  #Step-4
    csvwr = csv.writer(fp) #Step-5
    #Here csvwr is an object f <class,csv.writer>
    #contains 2 Functions 1. writerow() 2. writerows()
    csvwr.writerow(colnames) #Step-6
    csvwr.writerows(records) #Step-7
    print("CSV File Created--verify")