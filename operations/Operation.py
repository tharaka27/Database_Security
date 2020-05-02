import configparser
import json


class Operation:
    def __init__(self):
        self.config = configparser.ConfigParser()
        





#op = Operation()
#op.execute()
'''
x = {
  "adrID": "1",
  "ID": "972401064V",
  "name": "Tharaka",
  "gender":"male",
  "phoneNum": "0772075287",
  "DoB":"1997/08/27"
}

y = json.dumps(x)
print(y)

config = configparser.ConfigParser()
config["Patients"] = {}
config["Patients"]["1"] = y

with open('database_data.ini', 'w+') as configfile:
            config.write(configfile)

            
config = configparser.ConfigParser()
config.read('database_data.ini')
print(config.sections())
print(config["Patients"]["1"])
print( json.loads(config["Patients"]["1"]) )
'''
