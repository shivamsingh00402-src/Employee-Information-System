#Program for Reading the Data from CSV File--reader() of csv module
#CSVFileReadEx1.py
import csv
with open("C:\\Users\\shiva\\PycharmProjects\\CSV\\Notes\\studentdata.csv",'r') as fp:
    csvr=csv.reader(fp) # Here csvr is an object of <class, _csv.reader>
    print("-" * 50)
    for record in csvr:
        for val in record:
            print("\t{}".format(val),end="\t")
        print()
    print("-"*50)