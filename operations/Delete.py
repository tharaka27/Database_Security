import configparser
import json
import sys

class Delete:
    def __init__(self):
        pass

    @staticmethod
    def deleteElemenet(table_name, element_id):
        config = configparser.ConfigParser()
        config.read('database_data.ini')
        
        config.remove_option(table_name, element_id)
        with open('database_data.ini', 'w') as f:
            config.write(f)

    @staticmethod
    def deleteRelation(table_name, relation):
        config = configparser.ConfigParser()
        config.read('database_data.ini')
        
        current  = config[table_name]["eid"]
        current  = current.split(",")

        current.remove(relation)
        current = ','.join(current)
        #print(current)
        config[table_name]["eid"] = current
        with open('database_data.ini', 'w') as f:
            config.write(f)

        

#-------------------------------
#
#     Example Usage
#
#-------------------------------
#Delete.deleteElemenet("Addresses", "6")
#Delete.deleteRelation("Managers", "6")
