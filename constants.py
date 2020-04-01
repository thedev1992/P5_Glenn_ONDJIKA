import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="" ,database="projet5")

CATEGORIES = ['spaghetti',
              'pizza',
              'fromage',

                        ]

quantity = 20


def save_presentation():
    print("\nMENU > Voulez-vous enregistrer cet aliment ? ")
    print("\n1 - Oui ")
    print("2 - Non, je veux choisir un autre aliment ")
    print("3 - Retourner au menu principal ")


def menu_presentation():
    print("\nMENU > Entrer le chiffre correspondant à votre choix. ")
    print("\n1 - Quel aliment souhaitez-vous remplacer ? ")
    print("2 - Retrouver mes aliments substitués ")
