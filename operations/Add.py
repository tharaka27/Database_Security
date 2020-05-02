import configparser
import json

class Add:
    def __init__(self):
        pass

    @staticmethod
    def addElemenet(table_name, data_dic):
        config = configparser.ConfigParser()
        config.read('database_data.ini')
        
        lastID = 1
        #let's find the last key of the table
        for key in config[table_name]:
            if lastID < int(key):
                lastID = int(key)
        print(lastID + 1)

        print(str(json.dumps(data_dic)))
        config[table_name][str(lastID + 1)] = json.dumps(data_dic)
        with open('database_data.ini', 'w') as f:
            config.write(f)

    @staticmethod
    def addRelation(table_name, relation):
        config = configparser.ConfigParser()
        config.read('database_data.ini')
        
        current  = config[table_name]["eid"]
        if current == "":
            current = relation
        else:
            c = current
            if len(current) == 1 and current == relation:
                return
            elif len(current) != 1 and relation in c.split(","):
                return
            current = current + "," + relation
        #print(current)
        config[table_name]["eid"] = current
        with open('database_data.ini', 'w') as f:
            config.write(f)

        

#-------------------------------
#
#     Example Usage
#
#-------------------------------
#data_dic = {"street": "Bulugahawatta Road5", "town": "Kadawatha5"}   
#Add.addElemenet("Addresses",data_dic)
#Add.addRelation("Administrators", "7")

