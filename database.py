import mysql.connector
from constants import *
from api import *


class DbManager:

    def __init__(self):
        self.connectdb()

    def createDatabase(self):
        try:
            self.mycursor = db.cursor()
            self.mycursor.execute("CREATE DATABASE ")
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
            self.mycursor.execute("""CREATE TABLE IF NOT EXISTS Category_product(
	                                id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	                                product_id BIGINT UNSIGNED NOT NULL,
                                    category_id SMALLINT UNSIGNED,
	                                CONSTRAINT fk_product_id_id
	                                        FOREIGN KEY (product_id)
	                               	        REFERENCES Product(code),
                                   	CONSTRAINT fk_category_id
	                            	        FOREIGN KEY (category_id)
	                            	        REFERENCES Category (id));
	                            	""")
        except Exception as e:
            return e

        try:
            self.mycursor.execute("""CREATE TABLE IF NOT EXISTS Store_product(
        	                                id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        	                                product_id BIGINT UNSIGNED NOT NULL,
                                            store_id SMALLINT UNSIGNED,
        	                                CONSTRAINT fk_product_id_id
        	                                        FOREIGN KEY (store_id)
        	                               	        REFERENCES store(code),
                                           	CONSTRAINT fk_category_id
        	                            	        FOREIGN KEY (product_id)
        	                            	        REFERENCES product (id));
        	                            	""")
        except Exception as e:
            return e

        try:
            self.mycursor.execute("""CREATE TABLE IF NOT EXISTS Favorite (
	                                product_id BIGINT UNSIGNED NOT NULL,
	                                substitute_id BIGINT UNSIGNED NOT NULL,
	                                date_heure DATETIME,
            	                    pseudo VARCHAR(30) NOT NULL,
	                                PRIMARY KEY(product_id, substitute_id, pseudo),
	                                CONSTRAINT fk_product_id_code
		                                    FOREIGN KEY (product_id)
		                                    REFERENCES Product(code),
	                                CONSTRAINT fk_substitute_id_code
		                                    FOREIGN KEY (substitute_id)
		                                    REFERENCES Product(code));
        	                            	""")
        except Exception as e:
            return e

    def insert_product(self,code,name,grade,url,description, *args):
        sql_insert_query = """INSERT IGNORE INTO Products (code, product_name_fr, nutrition_grade_fr, url, generic_name_fr)\
                                      VALUES (%s, %s, %s, %s, %s)"""
        self.mycursor.execute(sql_insert_query, (code, name, grade, url, description))


    def insert_store(self, stores,*args):
        for store in stores:
            sql_insert_query = """ INSERT INTO Store (store_name) VALUES (%s)"""
            self.mycursor.execute(sql_insert_query, (store,))


    def insert_rows(self, products):
        for product in products:
            self.insert_product(*product)
            self.insert_store(*product)

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