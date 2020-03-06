import mysql.connector
import constants


class DbManager:

    def __init__(self):
        self.connectdb()

    def createDatabase(self):
        try:
            dbcreator = mysql.connector.connect(host="localhost", user="root", password="")
            self.mycursor = dbcreator.cursor()
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
                self.mycursor.execute("CREATE TABLE IF NOT EXISTS category( `id` INT NOT NULL AUTO_INCREMENT , `name` VARCHAR(25) NOT NULL , PRIMARY KEY (`id`), UNIQUE `UNIQUE` (`name`)) ENGINE = InnoDB;")
            except Exception as e:
                return e
            try:
                self.mycursor.execute("CREATE TABLE IF NOT EXISTS subtitute( `id` INT NOT NULL AUTO_INCREMENT , `f name` VARCHAR(32) NOT NULL , `f_url` VARCHAR(125) NOT NULL , `f_description` TINYTEXT NOT NULL , `reg_date` DATE NULL , `mod_date` DATE NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;")
            except Exception as e:
                return e

    def showdb(self):
        self.mycursor = db.cursor()
        self.mycursor.execute("SHOW TABLES")
        for tb in self.mycursor:
            print(tb)