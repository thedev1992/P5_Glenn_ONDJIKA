import random
import mysql.connector
from database import DbManager
from api import *
from user import *
from function_main import *


def product_menu(products):

    choice = input("\nEntrez le numéro de l'aliment : ")
    if int(choice) <= len(products):
        proposition = db_product.proposition(choice)
        if proposition:
            save_menu(choice, proposition)
        else:
            product_menu(products)

product_menu(10)