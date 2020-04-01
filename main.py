import random
import mysql.connector
from database import DbManager
from api import *
from user import *
from function_main import category_menu

db = Category()
save = Save()
"""
main_loop = True


def main():

    main_loop = True

    while main_loop:
        print("\nMENU > Entrer le chiffre correspondant à votre choix. ")
        print("\n1 - Quel aliment souhaitez-vous remplacer ? ")
        print("2 - Retrouver mes aliments substitués ")

        choice = int(input("\n Votre choix: "))
        if choice == 1:
            categories = db.show_category()
            category_menu(categories)

        elif choice == 2:
            save.show_new_products()

        else:
            print("Erreur : Entrer un numéro valide.")



if __name__ == '__main__':
    main()"""

save.proposition()

