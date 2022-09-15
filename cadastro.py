import pickle
import os
from time import sleep
from validacoes import *






def registuser():
    while True:
        option = ' '
        os.system("clear")
        print('''
            
        | ================================================================ |
        | ---------------------- User Registration ---------------------- |
        |                                                                 |
        |                       1 - Register User                         |           
        |                       2 - Edit User                             |
        |                       3 - Search User                           |
        |                       4 - Remove User                           |
        |                       5 - Back to Menu                          |
        |                                                                 |
        | --------------------------------------------------------------- |
        | =============================================================== |
        
            ''')
        option = input("Choose an option: ")
        
        if option == '1':
            cadasteruser()
        elif option == '2':
            edituser()
        elif option == '3':
            search()
        elif option == '4':
            remove()
        elif option == '5':
            break
        else:
            print("Invalid Option!")


# ------------------------------ Def Save Arquive --------------------------------------- #

def listclient():
    try:
        clientreg = open("clientpantry.dat", "rb")
        regbox = pickle.load(clientreg)
        clientreg.close()
    except:
        clientreg = open("clientpantry.dat", "wb")
        clientreg.close()
    return regbox

def gravclient(regbox):
    clientreg = open("clientpantry.dat", "wb")
    pickle.dump(regbox, clientreg)
    clientreg.close()
    
    
regbox = {}





# ------------------------------ Register User Function ---------------------------------------- #


def cadasteruser():
    os.system("clear")
   
    print('''
    
    | --------------------- Welcome to the Register -------------------------- |
    | ======================================================================== |
    | >>> Please inform your data                                          <<< |
    | ======================================================================== |
    | >>> Name:                                                            <<< |
    | >>> Birth Date:                                                      <<< |
    | >>> Email:                                                           <<< |
    | >>> CPF:                                                             <<< |
    | >>> Address:                                                         <<< |
    | >>> Sex:                                                             <<< |
    | >>> Blood Type:                                                      <<< |
    | >>> Additional Features:                                             <<< |
    | ======================================================================== |
        
        ''')
    while True:
        name = input("Type your name: ")
        if validstring(name):
            break
        else:
            print("Invalid name!")
    while True:
        birth = input("Type your birth date: ")
        if data_valida(birth):
            break
        else:
            print("Invalid date!")
    while True:
        email = input("Type your email: ")
        if validemail(email):
            break
        else:
            print("Invalid email")
    adress = input("Type your adress: ")
    while True:
        sex = input("Type your sex: ")
        if validstring(sex):
            break
        else:
            print("Sex Invalid!")
    while True:
        blood = input("Type blood type: ")
        if validstring(blood):
            break
        else:
            print("Invalid Blood!")
    features = input("Type additionais comments: ")
    while True:        
        cpf = input("Type your CPF: ")
        if cadastrocpf(cpf):
            print("Verified CPF!")
            while True:
                if cpf not in regbox:
                    regbox[cpf] = [name, birth, email, adress, sex, blood, features]
                    print("Congratulations, your registration was successful!")
                    gravclient(regbox)
                    conti = input("Press ENTER for continue... ")  
                    registuser()  
                else:
                    print("CPF not found!")
                    break  
           
        else:
            print("Invalid CPF!")
    
    
     
    
def edituser():
    while True:
        os.system("clear")
        print('''
        
        | --------------------- Welcome to the Edit ------------------------------ |
        | ======================================================================== |
        | >>> We Will Edit Your Information                                    <<< |
        | ======================================================================== |
        | >>> New Name:                                                        <<< |
        | >>> New Birth Date:                                                  <<< |
        | >>> New Email:                                                       <<< |
        | >>> New Address:                                                     <<< |
        | >>> New Sex:                                                         <<< |
        | >>> New Blood Type:                                                  <<< |
        | >>> New Additional Features:                                         <<< |
        | ======================================================================== |
            
            ''')
        cpf = input("Insert your CPF: ")
        if cadastrocpf(cpf):
            if cpf not in regbox:
                print("CPF not registred!")
                registuser()
            else:
                print("CPF Found!")
                print("Loading...")
                sleep(1)
                os.system("cls")
                while True:
                    newreg = input("what information do you want to change: ")
                    while True:
                        if newreg == "name":
                            newname = input("Enter a new name: ")
                            if validstring(newname):
                                regbox[cpf][0] = newname
                                print("New name registered sucessfully!")
                                gravclient(regbox)
                                break
                            else:
                                print("Invalid name!")
                    while True:
                        if newreg == "birth":
                            newbirth = input("Enter a new birth date: ")
                            if data_valida(newbirth):
                                regbox[cpf][1] = newbirth
                                print("New date of birth sucessfully added!")
                                gravclient(regbox)
                                break
                            else:
                                print('Invalid date!')
                    while True:
                        if newreg == "email":
                            newemail = input("Enter a new email: ")
                            if validemail(newemail):
                                regbox[cpf][2] = newemail
                                print("New email successfully registered!")
                                gravclient(regbox)
                                break
                            else:
                                print("Invalid email!")
            
                        if newreg == "address":
                            newaddress = input("Enter your new address: ")
                            regbox[cpf][3] = newaddress
                            print("New address successfully registered!")
                            gravclient(regbox)
                            break
                    while True:
                        if newreg == "sex":
                            newsex = input("Enter your new sex: ")
                            if validstring(newsex):
                                regbox[cpf][4] = newsex
                                print("New sex successfulyl registered!")
                                gravclient(regbox)
                                break
                            else:
                                print("Invalid sex!")
                   
                        if newreg == "blood":
                            newblood = input("Enter your new blood type: ")
                            regbox[cpf][5] = newblood
                            print("New bloody type successfully registered!")
                            gravclient(regbox)
                            break
                            
                        if newreg == "features":
                            newfeatures = input("Enter your new features: ")
                            regbox[cpf][6] = newfeatures
                            print("New features successfully registered!")
                            gravclient(regbox)
                            break
                        else:
                            print("Invalid option!")
                                    
                            
                                
                
        
            
def search():
    while True:
        os.system("clear")
        cpf = input("Enter the CPF of the user you want to search: ")
        if cadastrocpf(cpf):
            if cpf not in regbox:
                print("CPF not found!")
                sleep(2)
                registuser()
            else:
                print(f'''
                | ===================================================================== |
                |                       SIG - Pantry Search                             |
                | --------------------------------------------------------------------- |                
                | CPF Found                                                             | 
                | ===================================================================== |      
                | --- Nome: {regbox[cpf][0]}                                                       |
                | --- Birth: {regbox[cpf][1]}                                                 |
                | --- Email: {regbox[cpf][2]}                                  |
                | --- Address: {regbox[cpf][3]}                                           |
                | --- Sex: {regbox[cpf][4]}                                                    |
                | --- Blood: {regbox[cpf][5]}                                                 |
                | --- Features: {regbox[cpf][6]}                                                  |
                |                                                                       |
                | ===================================================================== |        
                
                ''')
                # as linhas do código acima ficaram desconexas por causa da formatação final do programa 
                conti = input("Press ENTER for continue...")
                registuser()
        else:
            print("CPF Invalid")
            print("teste")


def remove():
    os.system("clear")
    cpf = input("Enter the CPF of the user you want to remove: ")
    if cadastrocpf(cpf):
        if cpf not in regbox:
            print("CPF not found")
            registuser()
        else:
            print("CPF FOund!")
            del regbox[cpf]
            print("Deleted User")
            conti = input("Press ENTER for continue...")
            registuser()
  