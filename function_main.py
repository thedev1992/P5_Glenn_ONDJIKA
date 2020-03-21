from database import *
from database import *
from user import *
from constants import *
from main import *

db_product = Category()
save = Save()

def category_menu(number_category):

    category_choice = input("\nEntrez le numéro de la catégorie: ")
    if category_choice in number_category:
        products = db_product.show_product(category_choice)
        product_menu(products)

    else:
        print("Erreur : Entrer un numéro valide.")
        category_menu(number_category)


def product_menu(products, category_choice):

    choice = input("\nEntrez le numéro de l'aliment : ")
    if choice in products:
        proposition = db_product.proposition(choice)
        if proposition:
            save.save_products(choice, proposition)
        else:
            product_menu(choice)

    else:
        print("Erreur : Entrer un numéro valide.")
        product_menu(products, category_choice)


def save_menu(product, new_product):

    print("\nMENU > Voulez-vous enregistrer cet aliment ? ")
    print("\n1 - Oui ")
    print("2 - Non, je veux choisir un autre aliment ")
    print("3 - Retourner au menu principal ")

    choice = input("\nVotre choix : ")
    if choice == "1":
        save.save_products(product, new_product)
        fmain()

    elif choice == "2":
        categories = db.show_category()
        category_menu(categories)

    elif choice == "3":
        fmain()

    else:
        print("Erreur : Entrer un numéro valide.")
        save_menu(product, new_product)