#Program for Converting JSON String Data into Dict Object Data.--by Using loads() of json module
#JsonDataToDictData.py
import json
jsondata='{"ENO":"100","NAME":"Rossum","SAL":"3.5"}'
print("Json Data={} Type={}".format(jsondata,type(jsondata)))
print("-----------------------------------------------------------")
dictdata=json.loads(jsondata)
print("Dict Data={} Type={}".format(dictdata,type(dictdata)))
for k,v in dictdata.items():
    print("\t{}----------{}".format(k,v))