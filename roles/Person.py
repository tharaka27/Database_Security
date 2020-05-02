import configparser

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
            self.table_list.append(key)
        
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
        pass

    def execute_action(self):
        pass
