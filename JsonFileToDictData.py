#Program for Reading the Content of JSON File  into Dict Object Data we use ---load() of json module
#JsonFileToDictData.py
import json
def readjsondata():
    try:
        with open("C:\\Users\\shiva\\PycharmProjects\\JSON\\Notes\\emp.json","r") as fp:
            dictdata = json.load(fp)
            print("Dict Data={} Type={}".format(dictdata,type(dictdata)))
    except FileNotFoundError:
        print("Json File Does Not Exist")
    else:
        for k,v in dictdata.items():
            print("\t {}--->{}".format(k,v))


#Main Program
readjsondata()