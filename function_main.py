from database import *
from database import *
from user import *
from constants import *


db_product = Category()
save = Save()


def category_menu(number_category):

    category_choice = input("\nEntrez le numéro de la catégorie: ")
    if category_choice in number_category:
        products = db_product.show_product(category_choice)

    else:
        print("Erreur : Entrer un numéro valide.")
        category_menu(number_category)


    choice = input("\nEntrez le numéro de l'aliment : ")

    if int(choice) <= len(products):
        db_product.proposition(choice)
        save_menu(category_choice, choice)
    else:
        print("Erreur : Entrer un numéro valide.")
        choice = input("\nEntrez le numéro de l'aliment : ")
        if int(choice) <= len(products):
            db_product.proposition(choice)
            print(choice)
            save_menu(category_choice, choice)


def save_menu(product, new_product):

    print("\nMENU > Voulez-vous enregistrer cet aliment ? ")
    print("\n1 - Oui ")
    print("2 - Non, je veux choisir un autre aliment ")
    print("3 - Retourner au menu principal ")

    choice = input("\nVotre choix : ")
    if choice == "1":
        save.save_products(product, new_product)
        main()

    elif choice == "2":
        categories = db.show_category()
        category_menu(categories)

    elif choice == "3":
        main()

    else:
        print("Erreur : Entrer un numéro valide.")
        save_menu(product, new_product)


