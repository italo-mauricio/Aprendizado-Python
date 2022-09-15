import os
from validacoes import *
from cadastro import *
from main import *

regbox2 = regbox



def alimentos():
    while True:
        option = ' '
        os.system("clear")
        print('''
                
            | =============================================================== |
            | ---------------------- Food Registration ---------------------- |
            |                                                                 |
            |                       1 - Register Food                         |           
            |                       2 - Edit Food                             |
            |                       3 - Search Food                           |
            |                       4 - Remove Food                           |
            |                       5 - Back to Menu                          |
            |                                                                 |
            | --------------------------------------------------------------- |
            | =============================================================== |
            
                ''')
        option = input("Choose your option: ")

        if option == 1:
            cadaalimento()
        elif option == 2:
            searchfood()
        elif option == 3:
            editfood()
        elif option == 4:
            removefood()
        elif option == 5:
            main()
        else:
            print("Invalid Option!")



# ========================== Function Save ============================ #

def listfood():
    try:
        foodreg = open("foodpantry.dat", "rb")
        regbox2 = pickle.load(foodreg)
        foodreg.close()
    except:
        foodreg = open("foodpantry.dat", "wb")
        foodreg.close()
    return regbox2

def gravfood(regbox):
    foodreg = open("foodpantry.dat", "wb")
    pickle.dump(regbox, foodreg)
    foodreg.close()
    
    
regbox2 = {}


# =============================== Function Reg Food ========================================= #

def cadaalimento():
    while True:
        os.system("clear")
        print('''
        
        | -------------------- Welcome to the Register Food ---------------------- |
        | ======================================================================== |
        | >>> Please inform your data                                          <<< |
        | ======================================================================== |
        | >>> Name Food:                                                       <<< |
        | >>> Due Date:                                                        <<< |
        | >>> Type of food:                                                    <<< |
        | >>> Calories:                                                        <<< |
        | >>> Additional Features:                                             <<< |
        | >>> Food ID:                                                         <<< |
        | ======================================================================== |
            
            ''')
        while True:
            namefood = input("Type food name: ")
            if validstring(namefood):
                break
            else:
                print("Invalid Food")
        while True:
            datefood = input("Type due date food: ")
            if data_valida(datefood):
                break
            else:
                print("Invalid date")
        while True:
            typefood = input("Type food type: ")
            if validstring(typefood):
                break
            else:
                print("Invalid type!")
        while True:
            calories = input("Type food calories: ")
            if validnum(calories):
                break
            else:
                print("Invalid Calories!")
        while True:
            factures = input("Type food features: ")
            if validstring(factures):
                break
            else:
                print("Invalid features!")
        while True:
            id = input("Type food ID (CPF format): ")
            if cadastrocpf(id):
                print("Valid ID!")
                regbox2[id] = [namefood, datefood, typefood, calories, factures]
                gravfood()
                print("Food Registed Sussefully!")
            else:
                print("Invalid ID")
 

# ================================================ Function Search ================================================================ #


def searchfood():
   while True:
        os.system("clear")
        id = input("Enter the ID of the user you want to search: ")
        if cadastrocpf(id):
            if id not in regbox2:
                print("ID not found!")
                sleep(2)
                registuser()
            else:
                print(f'''
                | ===================================================================== |
                |                       SIG - Pantry Search                             |
                | --------------------------------------------------------------------- |                
                | ID Found                                                              | 
                | ===================================================================== |      
                | --- Name Food: {regbox2[id][0]}                                                       |
                | --- Expiration Date: {regbox2[id][1]}                                                 |
                | --- Type Food: {regbox2[id][2]}                                  |
                | --- Calories: {regbox2[id][3]}                                           |
                | --- Features: {regbox2[id][4]}                                                    |
                |                                                                       |
                | ===================================================================== |        
                
                ''')
                # as linhas do código acima ficaram desconexas por causa da formatação final do programa 
                conti = input("Press ENTER for continue...")
                registuser()
        else:
            print("ID Invalid")


# ==================================== Function Remove Food ================================================== #


def removefood():
    os.system("clear")
    id = input("Enter the ID of the user you want to remove: ")
    if cadastrocpf(id):
        if id not in regbox2:
            print("Food not found")
            registuser()
        else:
            print("CPF FOund!")
            del regbox2[id]
            print("Deleted User")
            conti = input("Press ENTER for continue...")
            registuser()

    
# ================================ Function Edit Food ========================================================= #


def editfood():
    while True:
        os.system("clear")
        print('''
        
        | --------------------------- Welcome to the Edit ----------------------------- |
        | ============================================================================= |
        | >>> We Will Edit Your Information                                         <<< |
        | ============================================================================= |
        | >>> New Name Food:                                                        <<< |
        | >>> New Expiration Date:                                                  <<< |
        | >>> New Type Food:                                                        <<< |
        | >>> New Calories Food:                                                    <<< |
        | >>> New Features:                                                         <<< |
        | ============================================================================= |
            
            ''')
        id = input("Insert your CPF: ")
        if cadastrocpf(id):
            if id not in regbox2:
                print("ID not registred!")
                registuser()
            else:
                print("ID Found!")
                print("Loading...")
                sleep(1)
                os.system("clear")
                while True:
                    newreg = input("what information do you want to change: ")
                    while True:
                        if newreg == "name":
                            newname = input("Enter a new name: ")
                            if validstring(newname):
                                regbox2[id][0] = newname
                                print(f'''

                                    | --------------------------- Welcome to the Edit ----------------------------- |
                                    | ============================================================================= |
                                    | >>> We Will Edit Your Information                                         <<< |
                                    | ============================================================================= |
                                    | >>> Name Food: {regbox2[id][0]}                                           <<< |
                                    | >>> Expiration Date: {regbox2[id][1]}                                     <<< |
                                    | >>> Type Food: {regbox2[id][2]}                                           <<< |
                                    | >>> Calories Food: {regbox2[id][3]}                                       <<< |
                                    | >>> Features: {regbox2[id][4]}                                            <<< |
                                    | ============================================================================= |
                                        
                                ''')
                                print("New name registered sucessfully!")
                                gravclient(regbox2)
                                break
                            else:
                                print("Invalid name!")
                    while True:
                        os.system("clear")
                        if newreg == "expiration":
                            newexp = input("Enter a new expiration date: ")
                            if data_valida(newexp):
                                regbox[id][1] = newexp
                                print(f'''

                                    | --------------------------- Welcome to the Edit ----------------------------- |
                                    | ============================================================================= |
                                    | >>> We Will Edit Your Information                                         <<< |
                                    | ============================================================================= |
                                    | >>> Name Food: {regbox2[id][0]}                                           <<< |
                                    | >>> Expiration Date: {regbox2[id][1]}                                     <<< |
                                    | >>> Type Food: {regbox2[id][2]}                                           <<< |
                                    | >>> Calories Food: {regbox2[id][3]}                                       <<< |
                                    | >>> Features: {regbox2[id][4]}                                            <<< |
                                    | ============================================================================= |
                                        
                                ''')
                                print("New date of expiration sucessfully added!")
                                gravclient(regbox2)
                                conti = input("Press ENTER for continue... ")
                                break
                            else:
                                print('Invalid date!')
                    while True:
                        os.system("clear")
                        if newreg == "type":
                            newtype = input("Enter a new type: ")
                            if validemail(newtype):
                                regbox[id][2] = newtype
                                print(f'''

                                    | --------------------------- Welcome to the Edit ----------------------------- |
                                    | ============================================================================= |
                                    | >>> We Will Edit Your Information                                         <<< |
                                    | ============================================================================= |
                                    | >>> Name Food: {regbox2[id][0]}                                           <<< |
                                    | >>> Expiration Date: {regbox2[id][1]}                                     <<< |
                                    | >>> Type Food: {regbox2[id][2]}                                           <<< |
                                    | >>> Calories Food: {regbox2[id][3]}                                       <<< |
                                    | >>> Features: {regbox2[id][4]}                                            <<< |
                                    | ============================================================================= |
                                        
                                ''')
                                print("New type successfully registered!")
                                gravclient(regbox2)
                                conti = input("Press ENTER for continue... ")
                                break
                            else:
                                print("Invalid email!")
                    while True:
                        os.system("clear")
                        if newreg == "calories":
                            if validnum(newreg):
                                newcalories = input("Enter your new calories value: ")
                                regbox2[id][3] = newcalories
                                print(f'''

                                    | --------------------------- Welcome to the Edit ----------------------------- |
                                    | ============================================================================= |
                                    | >>> We Will Edit Your Information                                         <<< |
                                    | ============================================================================= |
                                    | >>> Name Food: {regbox2[id][0]}                                           <<< |
                                    | >>> Expiration Date: {regbox2[id][1]}                                     <<< |
                                    | >>> Type Food: {regbox2[id][2]}                                           <<< |
                                    | >>> Calories Food: {regbox2[id][3]}                                       <<< |
                                    | >>> Features: {regbox2[id][4]}                                            <<< |
                                    | ============================================================================= |
                                        
                                ''')
                                print("New calories successfully registered!")
                                gravclient(regbox2)
                                conti = input("Press ENTER for continue... ")
                                break
                            else:
                                print("Invalid Calories")
                 
                            
                        if newreg == "features":
                            os.system("clear")
                            newfeatures = input("Enter your new features: ")
                            regbox[id][6] = newfeatures
                            print(f'''

                                | --------------------------- Welcome to the Edit ----------------------------- |
                                | ============================================================================= |
                                | >>> We Will Edit Your Information                                         <<< |
                                | ============================================================================= |
                                | >>> Name Food: {regbox2[id][0]}                                           <<< |
                                | >>> Expiration Date: {regbox2[id][1]}                                     <<< |
                                | >>> Type Food: {regbox2[id][2]}                                           <<< |
                                | >>> Calories Food: {regbox2[id][3]}                                       <<< |
                                | >>> Features: {regbox2[id][4]}                                            <<< |
                                | ============================================================================= |
                            ''')   
                            print("New features successfully registered!")
                            gravclient(regbox)
                            conti = input("Press ENTER for continue... ")
                            break
                        else:
                            print("Invalid option!")
                                    


