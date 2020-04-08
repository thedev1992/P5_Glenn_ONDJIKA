import random
import mysql.connector
from database import DbManager
from api import *
from user import *


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
            for id, category in categories:
                print(id, "-", category)
            category_menu(categories)

        elif choice == 2:
            saved_product = save.show_new_products()
            if not saved_product:
                print("\nVous n'avez rien enregistré.")

            for product_name, substitutes_name in zip(saved_product, saved_product):
                print(product_name[0], "a été remplacé par", substitutes_name[0], ".")

        else:
            print("Erreur : Entrer un numéro valide.")


def category_menu(number_category):
    category_loop = True

    while category_loop:
        category_choice = input("\nEntrez le numéro de la catégorie: ")
        if category_choice in number_category:
            product_menu()

        else:
            print("Erreur : Entrer un numéro valide.")


def product_menu():
    print('\n ------------------ Choisissez un aliment à remplaçer -------------------')
    products = db.show_product()
    x = 1
    print("Voici la sélection de produits : ")
    for result in products:
        print(x, ':', result[0])
        x += 1

    choices = input("\nEntrez le numéro de l'aliment : ")
    product_chosen = db.product_chosen(choices)
    for name in product_chosen:
        print("\nle produit choisis est :", name[0])

    if int(choices) <= len(products):
        proposition = save.proposition()
        random_product = random.choice(proposition)
        print('ID du produit de substitution: ', random_product[0], '\n',
              'Pour remplacer ce produit, nous vous proposons : ', random_product[1], '\n',
              'La description de ce produit est : ', random_product[3], '\n',
              'Il est disponible dans le(s) magasin(s) suivant(s) : ', random_product[4], '\n',
              'Son url est la suivante : ', random_product[2])

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



