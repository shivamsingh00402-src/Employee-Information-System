#Program for Converting Dict object Data into JSON String Data by Using str()
#DictDataToJsonData.py
import json
dictdata={'ENO':'100','NAME':'Rossum','SAL':'3.5'}
print("Dict Data={} Type={}".format(dictdata,type(dictdata)))
print("------------------------------------------------------------")
jsondata = str(dictdata)
print("Json Data={} Type={}".format(jsondata,type(jsondata)))