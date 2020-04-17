# import sql connector for databases
import mysql.connector
# object of database connection
db = mysql.connector.connect(host="localhost", user="root", password="" ,database="projet5")
# categories parameters for api requests
CATEGORIES = ['spaghetti',
              'pizza',
              'fromage',

                        ]
# quantity of product asked
quantity = 20

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
