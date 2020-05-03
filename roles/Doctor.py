from roles.Person import Person

class Doctor(Person):
    
    def __init__(self, fname, lname):
        Person.firstname = fname
        Person.lastname = lname
        Person.role = "Doctor"
        Person.table_list = []
        Person.access = {}
            
    

    def execute_action(self):
        print("1. Print hello world")

           


#x = Doctor("John", "Doe")
#print(x.getfname())
#print(x.getrole())
#x.load_settings()
#print(x.getaccessdic())
#x.print_possible_actions()
#x.actions_on("Prescriptions")

#print(x.execute("Prescriptions", 'Search', "1"))
#data_dic = {"eID": "2", "patID": "2", "description": "Fever3", "cost": "1503", "date": "2020/05/02", "time": "13:32", "prescription": "acetaminophen2"}

#print(x.execute("Prescriptions", 'Add', data_dic))
#print(x.execute("Prescriptions", 'Delete', "3"))

#up_dic = {"eID": "2", "patID": "2", "description": "Fever2", "cost": "1502", "date": "2020/05/03", "time": "13:32", "prescription": "acetaminophen2"}

#print(x.execute("Prescriptions", 'Update', "2", up_dic))
