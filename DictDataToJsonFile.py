#Program for Saving the Content of Dict Object Data into the JSON File we use ---dump() of json module
#DictDataToJsonFile.py
import json
dictdata = {'ENO':'100','NAME':'Rossum','SAL':'3.5'}
print("Dict Data={} Type={}".format(dictdata,type(dictdata)))
print("-----------------------------------------------------")
with open("C:\\Users\\shiva\\PycharmProjects\\JSON\\Notes\\emp.json","w")as fp:
    json.dump(dictdata,fp)
    print("Dict Data Saved in Json File---verify")
    
