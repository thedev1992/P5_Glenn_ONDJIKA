import random
import mysql.connector
from database import DbManager
from api import *
from user import *
from function_main import *

db = Category()


main_loop = True

def fmain():

    main_loop = True

    while main_loop:
        print("\nMENU > Entrer le chiffre correspondant à votre choix. ")
        print("\n1 - Quel aliment souhaitez-vous remplacer ? ")
        print("2 - Retrouver mes aliments substitués ")

        choice = int(input("\n Votre choix: "))
        if choice == 1:
            categories = db.show_category()
            category_menu(categories)

        else:
            print("Erreur : Entrer un numéro valide.")
            fmain()

        main_loop = False



fmain()