import random
import mysql.connector
from database import DbManager
from api import *
from user import *
from function_main import *

db = Category()
save = Save()

def main():

    main_loop = True

    while main_loop:
        menu_presentation()

        choice = int(input("\n Votre choix: "))
        if choice == 1:
            print('\n ------------------ Choisissez une categories -------------------')
            categories = db.show_category()
            category_menu(categories)

        elif choice == 2:
            save.show_new_products()

        else:
            print("Erreur : Entrer un numéro valide.")


def category_menu(number_category):

    category_choice = input("\nEntrez le numéro de la catégorie: ")
    if category_choice in number_category:
        product_menu()

    else:
        print("Erreur : Entrer un numéro valide.")
        category_menu(number_category)


def product_menu():
    print('\n ------------------ Choisissez un aliment à remplaçer -------------------')
    products = db_product.show_product()
    choices = input("\nEntrez le numéro de l'aliment : ")
    db.product_chosen(choices)

    if int(choices) <= len(products):
        save.proposition()
        save_presentation()
        choice = input("\nVotre choix : ")
        if choice == "1":
            id_substitut = input("Entrer l'ID du substitut afin de l'enregistrer:  ")
            save.save_menu(choices, id_substitut)

        elif choice == "2":
            categories = db.show_category()
            category_menu(categories)

        else:
            print("Erreur : Entrer un numéro valide.")
            product_menu()

    else:
        print("Erreur : Entrer un numéro valide.")
        product_menu()


if __name__ == '__main__':
    main()



