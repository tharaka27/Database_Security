from roles.Person import Person

class Nurse(Person):
    
    def __init__(self, fname, lname):
        Person.firstname = fname
        Person.lastname = lname
        Person.role = "Nurse"
        Person.table_list = []
        Person.access = {}
            
    

    def execute_action(self):
        print("1. Print hello world")

           


#x = Nurse("John", "Doe")
#print(x.getfname())
#print(x.getrole())
#x.load_settings()
#print(x.getaccessdic())
