import configparser
import json

class Update:
    def __init__(self):
        pass

    @staticmethod
    def updateElemenet(table_name, ID , data_dic):
        config = configparser.ConfigParser()
        config.read('database_data.ini')
        
        config[table_name][str(ID)] = json.dumps(data_dic)
        with open('database_data.ini', 'w') as f:
            config.write(f)

    @staticmethod
    def updateRelation(table_name, new_relation):
        config = configparser.ConfigParser()
        config.read('database_data.ini')
        
        config[table_name]["eid"] = new_relation
        with open('database_data.ini', 'w') as f:
            config.write(f)   

#-------------------------------
#
#     Example Usage
#
#-------------------------------
data_dic = {"street": "Bulugahawatta Road5", "town": "Kadawatha6"}   
Update.updateElemenet("Addresses", "5" ,data_dic)

data_dic = "5,6" 
Update.updateRelation("Managers", data_dic)

