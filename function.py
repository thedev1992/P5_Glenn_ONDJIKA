from user import Save
import random
from category import Product

"""
    function presentation of principal menu and description 
    of the users choices.

"""


def save_presentation():
    print("\nMENU > Voulez-vous enregistrer cet aliment ? ")
    print("\n1 - Oui ")
    print("2 - Non, je veux choisir un autre aliment ")
    print("3 - Retourner au menu principal ")


def menu_presentation():
    print("\nMENU > Entrer le chiffre correspondant à votre choix. ")
    print("\n1 - Quel aliment souhaitez-vous remplacer ? ")
    print("2 - Retrouver mes aliments substitués ")


save = Save()


def result_proposition():
    proposition = save.selected_by_nutrition_grade_d()
    random_product = random.choice(proposition)
    print('ID du produit de substitution: ', random_product[0], '\n',
          'Pour remplacer ce produit, nous vous proposons : ', random_product[1], '\n',
          'La description de ce produit est : ', random_product[3], '\n',
          'Il est disponible dans le(s) magasin(s) suivant(s) : ', random_product[4], '\n',
          'Son url est la suivante : ', random_product[2])


def result_proposition_b():
    proposition = save.selected_by_nutrition_grade_b()
    random_product = random.choice(proposition)
    print('ID du produit de substitution: ', random_product[0], '\n',
          'Pour remplacer ce produit, nous vous proposons : ', random_product[1], '\n',
          'La description de ce produit est : ', random_product[3], '\n',
          'Il est disponible dans le(s) magasin(s) suivant(s) : ', random_product[4], '\n',
          'Son url est la suivante : ', random_product[2])


product = Product()


def substitute_propostion(choices):
    for product_propostion in product.product_chosen(choices):
        if str(product_propostion[0]) <= 'd':
            result_proposition()
        elif str(product_propostion[0]) == 'a' or 'b':
            result_proposition_b()
    return choices
