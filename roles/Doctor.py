from Person import Person

class Doctor(Person):
    
    def __init__(self, fname, lname):
        Person.firstname = fname
        Person.lastname = lname
        Person.role = "Doctor"
        Person.table_list = []
        Person.access = {}
            
    def print_possible_actions(self):
        print("1. Print hello world")

    def execute_action(self):
        print("1. Print hello world")

           


x = Doctor("John", "Doe")
print(x.getfname())
print(x.getrole())
x.load_settings()
print(x.getaccessdic())
