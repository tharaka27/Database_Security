import configparser
import json
import sys

class Search:
    def __init__(self):
        self.config = configparser.ConfigParser()

    @staticmethod
    def findbyID(table_name, item_id):
        config = configparser.ConfigParser()
        config.read('database_data.ini')
        return json.loads(config[table_name][item_id])

    @staticmethod
    def isExist(table_name, item_id):
        config = configparser.ConfigParser()
        config.read('database_data.ini')
        resultset = config[table_name]["eid"].split(",")

        if item_id in resultset:
            return True
        else:
            return False
    
    @staticmethod
    def findbyName(table_name, column_name, item):
        config = configparser.ConfigParser()
        config.read('database_data.ini')
        resultset = []

        try:
            for key in config[table_name]:
                table = json.loads(config[table_name][key])
                if(table[column_name] == item):
                    table["item_ID"] = key
                    resultset.append(table)
        except:
            print("error occured. possible error - key error")
        return resultset

#-------------------------------
#
#     Example Usage
#
#-------------------------------
    
#print(Search.findbyID("Patients","1"))
#print(Search.findbyName("Employees","gender", "female"))
#print(Search.isExist("Doctors","4"))


