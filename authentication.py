import configparser
import os.path
from os import path
import hashlib

def main():
    
    #if(path.exists('database_roles.ini')):
    #    os.remove('database_roles.ini')
    #    print("File Removed!")

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
        input("press any key to continue")
   

if __name__== "__main__":
    user_role = "";
    main()
