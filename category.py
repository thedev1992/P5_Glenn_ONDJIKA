import mysql.connector
from database import DbManager


"""
    Make requests in the database.
"""


class Category(DbManager):
    """
        this class inherit from Dbmanger class.
        This class performs operations in the table class : Category, product.
    """

    def show_category(self):
        """ Display categories. """

        self.mycursor.execute(""" SELECT id, category_name from category WHERE id ORDER BY id LIMIT 6 ; """)
        results = self.mycursor.fetchall()

        return results


class Product(DbManager):

    def show_product(self):

        """ Display the products of a category. """

        self.mycursor.execute("""SELECT product_name_fr, code \
                FROM Products \
                INNER JOIN products_categories_key\
                ON Products.code = products_categories_key.product_id \
                INNER JOIN Category ON \
                Category.id = products_categories_key.category_id \
                WHERE category_id LIMIT 15 """)
        myresult = self.mycursor.fetchall()

        return myresult

    def product_chosen(self, _id):

        """ Display the selected product. """

        self.mycursor.execute("""SELECT product_name_fr \
                        FROM Products \
                        INNER JOIN products_categories_key\
                        ON Products.code = products_categories_key.product_id \
                        INNER JOIN Category ON \
                        Category.id = products_categories_key.category_id \
                        WHERE category_id =%s  LIMIT 15 """, (_id,))
        myresult = self.mycursor.fetchall()
        return myresult
