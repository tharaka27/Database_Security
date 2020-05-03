import configparser
from os import path
import hashlib
import sys
import json

from roles.Administrator import Administrator
from roles.Doctor import Doctor
from roles.Nurse import Nurse
from roles.Patient import Patient

def main():
    if(not(path.exists('database_roles.ini'))):
        config = configparser.ConfigParser()
        config['DEFAULT'] = {'isConfigured': 'True'}

        admin_username = input("Please input administartor username: ")
        admin_password = input("Please input administartor password: ")

        admin_password = hashlib.md5(admin_password.encode()).hexdigest()
        config['Administrator'] = {admin_username: admin_password}

        config['Doctor'] = {}
        config['Nurse'] = {}
        config['Patient'] = {}
        config['Manager'] = {}
        

        with open('database_roles.ini', 'w') as configfile:
            config.write(configfile)


    else:
        config = configparser.ConfigParser()
        config.read('database_roles.ini')
        username = input("Please input username: ")
        password = input("Please input password: ")
        password = hashlib.md5(password.encode()).hexdigest()

        if(username in config['Administrator']):
            if( config['Administrator'][username] == password ):
                user_role = 'Administrator';
            else:
                print("Wrong credentials")
                exit(0)
                

        elif(username in config['Doctor']):
            if( config['Doctor'][username] == password ):
                user_role = 'Doctor';
            else:
                print("Wrong credentials")
                exit(0)

        elif(username in config['Nurse']):
            if( config['Nurse'][username] == password ):
                user_role = 'Nurse';
            else:
                print("Wrong credentials")
                exit(0)

        elif(username in config['Patient']):
            if( config['Patient'][username] == password ):
                user_role = 'Patient';
            else:
                print("Wrong credentials")
                exit(0)

        else:
            print("Unsuccessfully login")
            exit(0)

        print("Successfully login as " + user_role)
        if(user_role == 'Administrator'):
            r = Administrator(username,"Ratnayake")
            
        elif(user_role == 'Doctor'):
            r = Doctor(username,"Ratnayake")
            
        elif(user_role == 'Nurse'):
            r = Nurse(username,"Ratnayake")
            
        elif(user_role == 'Patient'):
            r = Patient(username,"Ratnayake")
            
        r.load_settings()

        string = ("1.Enter 'help' to view possible functionality\n2.Enter 'Search' to search a data\n"
                  "3.Enter 'Add' to add new data\n4.Enter 'Update' to update existing data\n"
                  "5.Enter 'Delete' to delete data\n6.Enter 'View' to view this again.\n>>>")

        #print(string, end="")
        while(True):
            x = input(string)
            if(x == "help"):
                r.print_possible_actions()
            elif(x == "Search"):
                x, y = map(str, input("Enter tablename<space>id:\n>>>").split(" "))
                print(r.execute(x, 'Search', y))
                print("\n\n")
                
            elif(x == "Add"):
                table_name = input("Enter tablename :\n>>>")
                if( r.isPossible(table_name, "Add")):
                    config_data = configparser.ConfigParser()
                    config_data.read('database_data.ini')
                    dic = json.loads(config_data[table_name]["1"])
                    lis = dic.keys()
                    data_dic = {}
                    for i in lis:
                        data_dic[i] = input("Please input "+ i + " : ")
                    print("The following data will be added to tabel")
                    print(data_dic)
                    r.execute(table_name, 'Add', data_dic)    
                        
                    
                else:
                    print("Sorry you can perform such action")

                
            elif(x == "Update"):
                table_name = input("Enter tablename :\n>>>")
                idv = input("Enter id :\n>>>")
                if( r.isPossible(table_name, "Update")):
                    config_data = configparser.ConfigParser()
                    config_data.read('database_data.ini')
                    dic = json.loads(config_data[table_name]["1"])
                    lis = dic.keys()
                    data_dic = {}
                    for i in lis:
                        data_dic[i] = input("Please input "+ i + " : ")
                    print("The following data will be updated")
                    print(data_dic)
                    r.execute(table_name, 'Update', data_dic, idv)
                
            elif(x == "Delete"):
                x, y = map(str, input("Enter tablename<space>id:\n>>>").split(" "))
                print(r.execute(x, 'Search', y))
                print("\n\n")
                
            elif(x == "View"):
                print(string)
            else:
                print("Wrong command enter again")
            
        
        input("press any key to continue")
   

if __name__== "__main__":
    #print (sys.path)
    
    
    user_role = "";
    main()
