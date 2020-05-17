import mysql.connector
from constants import *
from api import Api


class DbManager:
    """
            This class has the responsibility of structuring
            the database, and inserting the data collection of the API
        """

    def __init__(self):
        """ Connect to Mysql database from the class DataBaseUser() """
        self.mycursor = db.cursor()
        self.connect_db()

    def create_database(self):
        """ Create Database """
        try:

            self.mycursor.execute("CREATE DATABASE IF NOT EXITS ")
            return True
        except Exception as e:
            return e

    def connect_db(self):
        """ Connection to database """
        try:
            self.mycursor = db.cursor()
            return True
        except Exception as e:
            return e

    def create_table(self):
        """ Create table Products """
        try:
            self.mycursor.execute("""CREATE TABLE IF NOT EXISTS products(
id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
code BIGINT UNSIGNED NOT NULL UNIQUE,
product_name_fr VARCHAR(150) NOT NULL ,
nutrition_grade_fr CHAR(1) NOT NULL,
url VARCHAR(400),
generic_name_fr VARCHAR(400)); """)
        except Exception as e:
            return e

        """ Create table store """
        try:
            self.mycursor.execute("""CREATE TABLE IF NOT EXISTS store(
id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
store_name VARCHAR(150) UNIQUE NOT NULL);""")
        except Exception as e:
            return e
        """ Create table category """
        try:
            self.mycursor.execute("""CREATE TABLE IF NOT EXISTS Category (
id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
ategory_name VARCHAR(150) UNIQUE);""")
        except Exception as e:
            return e

        """ Creating to the associate index table """
        try:
            self.mycursor.execute(""" CREATE TABLE IF NOT EXISTS Products_categories_key ( 
                                        id MEDIUMINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                                        product_id BIGINT REFERENCES Products(barcode),
                                        category_id MEDIUMINT REFERENCES UNIQUE Category(id));
                                     """)
        except Exception as e:
            return e

        try:
            self.mycursor.execute(""" CREATE TABLE IF NOT EXISTS Products_stores (
                                        id MEDIUMINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                                        product_id BIGINT REFERENCES Products(barcode),
                                        store_id MEDIUMINT REFERENCES Stores(id));               
                                     """)
        except Exception as e:
            return e

        """ Create the favorites table """

        try:
            self.mycursor.execute(""" CREATE TABLE IF NOT EXISTS Favorites (
                                        id_product BIGINT REFERENCES Products(barcode), 
                                        id_substitute BIGINT REFERENCES Products(barcode),
                                        PRIMARY KEY (id_product, id_substitute));                       
                                  """)
        except Exception as e:
            return e

    def insert_product(self, id, name, grade, url, description, *args):
        """ Insert the product data in the table
        """
        sql_insert_query = """INSERT IGNORE INTO Products (code, product_name_fr, nutrition_grade_fr, url, generic_name_fr)\
                                      VALUES (%s, %s, %s, %s, %s)"""
        self.mycursor.execute(sql_insert_query, (id, name, grade, url, description))

    def insert_store(self, id, name, grade, url, description, store, *args):
        """ Insert the store list data in the table"""

        sql_insert_query = """INSERT IGNORE INTO store(store_name) VALUES (%s)"""
        self.mycursor.execute(sql_insert_query, (store,))

        self.mycursor.execute(""" SELECT id FROM Store WHERE store_name=%s """, (store,))
        store_fetch = self.mycursor.fetchall()
        sql_insert_query2 = """INSERT INTO products_stores (product_id, store_id) VALUES (%s, %s) """
        self.mycursor.execute(sql_insert_query2, (id, store_fetch[0][0]))

    def insert_category(self, id, name, grade, url, categories, stores, *args):
        """ Insert the category list data in the table"""
        sql_insert_query = """INSERT IGNORE INTO Category(category_name) VALUES (%s)"""
        self.mycursor.execute(sql_insert_query, (categories,))

        self.mycursor.execute(""" SELECT id FROM category WHERE category_name=%s""", (categories,))
        category_fetch = self.mycursor.fetchall()
        sql_insert_query3 = """ INSERT INTO Products_categories_key (product_id, category_id) VALUES (%s, %s) """
        self.mycursor.execute(sql_insert_query3, (id, category_fetch[0][0]))

    def insert_rows(self, products):
        """ Execute the creating table """

        for product in products:
            self.insert_category(*product)
            self.insert_store(*product)
            self.insert_product(*product)
        print(
            "**** Insert data success *****"
        )
        return True

    def showdb(self):
        """ show the created table"""
        self.mycursor = db.cursor()
        self.mycursor.execute("SHOW TABLES")
        for tb in self.mycursor:
            print(tb)


def main():
    db = DbManager()
    db.create_database()
    db.create_table()
    data_collect = Api()
    api_connection = data_collect.connect_and_sort()
    final_product = data_collect.final_response(api_connection)
    db.insert_rows(final_product)
    db.showdb()


if __name__ == "__main__":
    main()
