import random
import mysql.connector
from constants import menu_presentation, save_presentation
from user import Category, Product, Save

"""
    This file starts the program.
"""

db = Category()
save = Save()
product = Product()


def main():

    main_loop = True

    while main_loop:
        """ Display the first menu. """
        menu_presentation()

        choice = input("\n Votre choix: ")

        if choice.isdigit(): # execute if the input is a number

            if int(choice) == 1:
                """ Display categories. """
                print('\n ------------------ Choisissez une categories -------------------')
                categories = db.show_category()
                categories_id = []
                for _id, category in categories:
                    categories_id.append(str(_id))
                    print(_id, "-", category)
                category_menu(categories_id)

            elif int(choice) == 2:
                saved_product = save.show_new_products()
                saved_substitute = save.substitute()
                if not saved_product:
                    print("\nVous n'avez rien enregistré.")

                for product_name, substitutes_name in zip(saved_product, saved_substitute):
                    print(product_name[0], "a été remplacé par", substitutes_name[0], ".")

        else:
            print("Erreur : Entrer un numéro valide.")


def category_menu(number_category):
    """
            This function is linked with
            choice_product to control the user input
    """
    category_loop = True

    while category_loop:
        """ Choice Category """
        category_choice = input("\nEntrez le numéro de la catégorie: ")
        if category_choice.isdigit():
            if category_choice in number_category:
                product_menu()

        else:
            print("Erreur : Entrer un numéro valide.")


def product_menu():
    """ Display products """
    second_loop = True
    while second_loop:
        print('\n ------------------ Choisissez un aliment à remplaçer -------------------')
        products = product.show_product()
        x = 1
        print("Voici la sélection de produits : ")
        for result in products:
            print(x, ':', result[0])
            x += 1

            """ Choice product """
        choices = input("\nEntrez le numéro de l'aliment : ")
        product_chosen = product.product_chosen(choices)
        for name in product_chosen:
            print("\nle produit choisis est :", name[0])
            print()

        """ Choose a product substitute and save in the data base """
        if int(choices) <= len(products):
            """ select the substitute with the best grades for the product """
            proposition = save.selected_by_nutrition_grade()
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
                main()

            elif choice == "2":
                print('\n ------------------ Choisissez une categories -------------------')
                categories = db.show_category()
                categories_id = []
                for _id, category in categories:
                    categories_id.append(str(_id))
                    print(_id, "-", category)
                category_menu(categories_id)

            elif choice == "3":
                main()

            else:
                print("Erreur : Entrer un numéro valide.")
                product_menu()

        else:
            print("Erreur : Entrer un numéro valide.")


if __name__ == '__main__':
    main()



