from database import *
from database import *
from user import *
from constants import *

db_product = Category()


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
        proposition = self.t_product.proposition(choice, category_choice)
                if proposition:
                    self.save_menu(choice, proposition)
        else:
            self.select_product_menu(products, category_choice)

        else:
            print("Erreur : Entrer un numéro valide.")
            self.select_product_menu(products, category_choice)


