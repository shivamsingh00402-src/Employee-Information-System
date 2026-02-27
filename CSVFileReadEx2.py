#Program for Reading the Data from CSV File--DictReader() of csv module
#CSVFileReadEx2.py
import csv
with open("C:\\Users\\shiva\\PycharmProjects\\CSV\\Notes\\studentdata.csv",'r') as fp:
    csvdr=csv.DictReader(fp) # Here csvr is an object of <class, csv.DictReader>
    for record in csvdr:
        for k,v in record.items():
            print("\t{}--->{}".format(k,v))
        print("---------------------------------------")