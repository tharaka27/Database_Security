import configparser
import sys

from operations.Add import Add
from operations.Update import Update
from operations.Delete import Delete
from operations.Search import Search

class Person:
    def __init__(self, fname, lname, role,table_list, access):
        self.firstname = fname
        self.lastname = lname
        self.role = role
        self.table_list = table_list
        self.access = access
        
    def getrole(self):
        return self.role

    def getlname(self):
        return self.lastname
    
    def getfname(self):
        return self.firstname

    def getaccessdic(self):
        return self.access

    def initialize_access_dic(self,table_list):
        access_rights = ["Search", "Delete", "Update", "Add"]
        for i in table_list:
            name = i + "_table"
            self.access[name] = {"Search" : False,
                                      "Delete" : False,
                                      "Update" : False,
                                      "Add" : False}
    def load_settings(self):
        config = configparser.ConfigParser()
    
        config.read('database_roles.ini')
        #print(config.sections())

        for key in config['Table_list']:
            self.table_list.append(key.capitalize())
        
        #print(self.table_list)
        self.initialize_access_dic(self.table_list)

        #print(self.access)

        for table_name in self.table_list:

            TABLE_NAME = table_name + "_table"
            table_access = config[TABLE_NAME][Person.role].split(",")
            #table_access = config[TABLE_NAME]["Administrator"].split(",")
            #print(TABLE_NAME , end= ' ')
            #print(table_access)
            if table_access == ['']:
                pass
            else:
                for i in table_access:
                    self.access[TABLE_NAME][i] = True

        #print(self.access)

    

    def print_possible_actions(self):
        actions = ['Search', 'Delete', 'Update', 'Add']

        print("you can perform,")
        counter = 1
        for key in self.access:
            for action in actions:
                if self.access[key][action]:
                    print( str(counter)+". " + action + " on table " + key)
                    counter = counter + 1
            

    def actions_on(self, table_name):
        actions = ['Search', 'Delete', 'Update', 'Add']

        print("you can perform ")
        counter = 1
        for action in actions:
            if self.access[table_name + "_table"][action]:
                print( str(counter)+ ". " + action)
                counter = counter + 1
        print("on table " + table_name)


    def isPossible(self,table_name, action):
        table_name = table_name + "_table"
        return self.access[table_name][action]

        
    def execute(self, table_name, action, *vartuple):
        #print(vartuple[0])
        if( self.isPossible(table_name, action)):
            if(action == 'Search'):
                return Search.findbyID(table_name,vartuple[0])

            elif(action == 'Delete'):
                Delete.deleteElemenet(table_name, vartuple[0])

            elif(action == 'Add'):
                Add.addElemenet(table_name,vartuple[0])

            elif(action == 'Update'):
                Update.updateElemenet(table_name, vartuple[0] ,vartuple[1])
            else:
               return("No such action exist.") 
            

        else:
            return("Sorry you donot have authority to perform such action.")


























        
        
