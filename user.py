import random
import mysql.connector
from database import DbManager
from api import *


class Category(DbManager):

    def show_category(self):
        self.mycursor.execute(""" SELECT id, category_name from category ORDER BY id; """)
        results = self.mycursor.fetchall()
        categories_id = []

        for _id, _category in results:
            categories_id.append(str(_id))
            print(_id, _category)
        return categories_id

    def show_product(self, id):
        self.mycursor.execute("""SELECT product_name_fr, code \
                FROM Products \
                INNER JOIN products_categories_key\
                ON Products.code = products_categories_key.product_id \
                INNER JOIN Category ON \
                Category.id = products_categories_key.category_id \
                WHERE category_id <= %s -2 """, (id,))
        myresult = self.mycursor.fetchall()
        x = 1
        print("Voici la sélection de produits : ")
        for result in myresult:
            print(x, ':', result[0])
            x += 1
        return myresult

    def proposition(self,category_id):

        self.mycursor.execute("""SELECT product_name_fr, url, generic_name_fr, store_name, code \
                    FROM Products \
                    INNER JOIN products_categories_key \
                    ON Products.code = products_categories_key.product_id \
                    INNER JOIN Category \
                    ON Category.id = products_categories_key.category_id \
                    INNER JOIN products_stores \
                    ON Products.code = products_stores.product_id \
                    INNER JOIN Store \
                    ON Store.id = products_stores.store_id \
                    WHERE category_id = %s""", (category_id,))
        myresult = self.mycursor.fetchall()
        random_product = random.choice(myresult)
        print('Pour remplacer ce produit, nous vous proposons : ', random_product[0], '\n',
              'La description de ce produit est : ', random_product[2], '\n',
              'Il est disponible dans le(s) magasin(s) suivant(s) : ', random_product[3], '\n',
              'Son url est la suivante : ', random_product[1])


class Save(DbManager):

    def save_products(self, product_id, new_product_id):
        """ Register products in the database. """
        try:
            self.mycursor.execute("""
                INSERT INTO favorites (id_product, id_substitute)
                VALUES (%s, %s)""",(product_id, new_product_id))
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

        if not product:
            print("\nVous n'avez rien enregistré.")

        for product_name, substitutes_name in zip(product, substitute):
            print(product_name[0], "a été remplacé par", substitutes_name[0],".")


def main():

    db = Category()
    db.show_product(4)


if __name__ == '__main__':
    main()

