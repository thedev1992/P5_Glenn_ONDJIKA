import mysql.connector
from constants import *
from api import *


class DbManager:

    def __init__(self):
        self.connectdb()

    def createDatabase(self):
        try:
            self.mycursor = db.cursor()
            self.mycursor.execute("CREATE DATABASE IF NOT EXITS ")
            return True
        except Exception as e:
            return e

    def connectdb(self):
        try:
            self.mycursor = db.cursor()
            return True
        except:
            return False

    def createTable(self):
        try:
            self.mycursor = db.cursor()
            self.mycursor.execute("""CREATE TABLE IF NOT EXISTS products(
	                                      id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	                                      code BIGINT UNSIGNED NOT NULL UNIQUE,
	                                      product_name_fr VARCHAR(150) NOT NULL ,
	                                      nutrition_grade_fr CHAR(1) NOT NULL,
	                                      url VARCHAR(400),
	                                      generic_name_fr VARCHAR(400)); 
	                                   """)
        except Exception as e:
            return e

        try:
            self.mycursor.execute("""CREATE TABLE IF NOT EXISTS store(
	                                 id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	                                 store_name VARCHAR(150) UNIQUE NOT NULL);
	                              """)
        except Exception as e:
            return e
        try:
            self.mycursor.execute("""CREATE TABLE IF NOT EXISTS Category (
    	                                 id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    	                                 category_name VARCHAR(150) UNIQUE);
    	                              """)
        except Exception as e:
            return e

        try:
            self.mycursor.execute(""" CREATE TABLE IF NOT EXISTS Products_categories_key ( 
                                        id MEDIUMINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                                        product_id BIGINT REFERENCES Products(barcode),
                                        category_id MEDIUMINT REFERENCES Category(id));
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

        try:
            self.mycursor.execute(""" CREATE TABLE IF NOT EXISTS Favorites (
                                        id_product BIGINT REFERENCES Products(barcode), 
                                        id_substitute BIGINT REFERENCES Products(barcode),
                                        PRIMARY KEY (id_product, id_substitute));                       
                                  """)
        except Exception as e:
            return e

    def insert_product(self,id,name, grade, url, description, *args):
        sql_insert_query = """INSERT IGNORE INTO Products (code, product_name_fr, nutrition_grade_fr, url, generic_name_fr)\
                                      VALUES (%s, %s, %s, %s, %s)"""
        self.mycursor.execute(sql_insert_query, (id, name, grade, url, description))

    def insert_store(self, id,name, grade, url, description, store, *args):
        print(store)
        sql_insert_query = """INSERT IGNORE INTO store(store_name) VALUES (%s)"""
        self.mycursor.execute(sql_insert_query, (store,))

        self.mycursor.execute(""" SELECT id FROM Store WHERE store_name=%s """,(store,))
        store_fetch = self.mycursor.fetchall()
        sql_insert_query2 = """INSERT INTO products_stores (product_id, store_id) VALUES (%s, %s) """
        self.mycursor.execute(sql_insert_query2, (id, store_fetch[0][0]))

    def insert_category(self,id, name, grade, url,categories, stores, *args):
        sql_insert_query = """INSERT IGNORE INTO Category(category_name) VALUES (%s)"""
        self.mycursor.execute(sql_insert_query, (categories,))
        
        self.mycursor.execute(""" SELECT id FROM category WHERE category_name=%s""", (categories,))
        category_fetch = self.mycursor.fetchall()
        sql_insert_query3 = """ INSERT INTO Products_categories_key (product_id, category_id) VALUES (%s, %s) """
        self.mycursor.execute(sql_insert_query3, (id, category_fetch[0][0]))

    def insert_rows(self, products):

        for product in products:
            self.insert_category(*product)
        print(
              "**** Insert data success *****"
              )
        return True

    def showdb(self):
        self.mycursor = db.cursor()
        self.mycursor.execute("SHOW TABLES")
        for tb in self.mycursor:
            print(tb)


def main():

    db = DbManager()
    #db.createDatabase()
    #db.createTable()
    data_collect = Api_data()
    api_connection = data_collect.connect_and_sort()
    final_product = data_collect.final_response(api_connection)
    db.insert_rows(final_product)


if __name__ == "__main__":
    main()