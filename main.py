import os
from time import sleep
from cadastro import *


def main():
    while True:
        option = ' '
        os.system("clear")
        print('''
        | ---------------------- SIG - Pantry --------------------------- | 
        | ------------------- Home Pantry Control ----------------------- |
        | --------------------------------------------------------------- |
        |                   1 - Register User                             |
        |                   2 - Register Foods                            |
        |                   3 - Monitoring                                |
        |                   4 - Infos                                     |     
        |                   4 - Exit the system                           |
        |                                                                 |
        |                                                                 |
        | --------------------------------------------------------------- |
        | ===================== By: Italo Dev =========================== |
        | =============================================================== |
        ''')
        option = input("Choose an option: ")
        
        if option == '1':
            registuser()
        elif option == '2':
            break
        elif option == '3':
            break
        elif option == '4':
            about()
        elif option == '5':
            break
        else:
            print("Invalid option!")
        

        
# =============================================================================================== #     
        
        
def about():
    os.system("clear")
    print(''' 
    | ========================= Project Informations =============================== |
    | ------------------------------------------------------------------------------ |
    | >>> Languange : Python 3.0.0                                               <<< |
    | >>> Autor : Italo Mauricio de Medeiros Santos                              <<< |
    | >>> Start Date : 30/08/2022                                                <<< |
    | >>> Description : The project aims to develop a CRUD in Python, in order   <<< |
    | >>> to increase knowledge about menus.                                     <<< |
    | >>> Enjoy!                                                                 <<< |
    ''') 
    input(">>> Press ENTER for continue... ")
       
    
    


main()