import sys
from roles.Person import Person

class Administrator(Person):
    
    def __init__(self, fname, lname):
        Person.firstname = fname
        Person.lastname = lname
        Person.role = "Administrator"
        Person.table_list = []
        Person.access = {}
            
    def execute_action(self):
        print("1. Print hello world")

           


#x = Administrator("John", "Doe")
#print(x.getfname())
#print(x.getrole())
#x.load_settings()
#print(x.getaccessdic())
