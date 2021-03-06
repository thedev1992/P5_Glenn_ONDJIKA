import mysql.connector
from database import DbManager
from api import *

"""
    Make requests in the database.
"""

class Save(DbManager):
    """ This class perform for the management of the saved product and the proposed product """

    """ propose a better nutriscore product to user """

    def selected_by_nutrition_grade_d(self):

        self.mycursor.execute(""" SELECT category_id, product_name_fr, url, generic_name_fr, store_name
         FROM Products INNER JOIN products_categories_key \
         ON Products.code = products_categories_key.product_id \
         INNER JOIN Category ON Category.id = products_categories_key.category_id \
         INNER JOIN products_stores ON Products.code = products_stores.product_id \
         INNER JOIN Store ON Store.id = products_stores.store_id \
         WHERE nutrition_grade_fr <= 'c'  ORDER BY `products_categories_key`.`category_id` ASC """)
        myresult = self.mycursor.fetchall()

        return myresult

    def selected_by_nutrition_grade_b(self):

        self.mycursor.execute(""" SELECT category_id, product_name_fr, url, generic_name_fr, store_name
         FROM Products INNER JOIN products_categories_key \
         ON Products.code = products_categories_key.product_id \
         INNER JOIN Category ON Category.id = products_categories_key.category_id \
         INNER JOIN products_stores ON Products.code = products_stores.product_id \
         INNER JOIN Store ON Store.id = products_stores.store_id \
         WHERE nutrition_grade_fr <= 'a'  ORDER BY `products_categories_key`.`category_id` ASC """)
        myresult = self.mycursor.fetchall()

        return myresult

    def save_menu(self,product_id,id_substitute):
        """ Register products in the database. """

        try:
            self.mycursor.execute("""
                INSERT INTO favorites (id_product, id_substitute)
                VALUES (%s, %s)""",(product_id, id_substitute))
            print("\nVotre choix est enregistré.")

        except mysql.connector.errors.IntegrityError as e:
            print(e)

    def show_new_products(self):
        """ Display the products registered in the database. """

        self.mycursor.execute("""SELECT product_name_fr\
                    FROM Products \
                    INNER JOIN products_categories_key \
                    ON Products.code = products_categories_key.product_id \
                    INNER JOIN Category \
                    ON Category.id = products_categories_key.category_id \
                    INNER JOIN favorites
                    ON category.id = favorites.id_product
                    WHERE category.id = favorites.id_product
                    """,)
        product = self.mycursor.fetchall()
        return product

    def substitute(self):
        """ Display the substitute registered in the database. """

        self.mycursor.execute("""SELECT product_name_fr\
                            FROM Products \
                            INNER JOIN products_categories_key \
                            ON Products.code = products_categories_key.product_id \
                            INNER JOIN Category \
                            ON Category.id = products_categories_key.category_id \
                            INNER JOIN favorites
                            ON category.id = favorites.id_substitute
                            WHERE category.id = favorites.id_substitute
                            """, )
        substitute = self.mycursor.fetchall()

        return substitute




