#coding:utf-8
import sys, pymysql, warnings


class DbManager:

    '''
        Classe de gestion des opérations sur la base données
    '''
    __host = "remotemysql.com"
    __user = "root"
    __password = ""
    __dbname = "projet5"

    '''
        Initialisation de la classe
    '''
    def __init__(self):
        self.dbConnect()
    
    '''
        Méthode de connexion de la base de données.
        Retourn l'instance de la connexio
    '''
    def dbConnect(self):
        # Tententive de la connexion à  la base de données
        try:
            db = pymysql.connect(self.__host, self.__user, self.__password, self.__dbname )
            # assignation de l'instance db a la var cursor
            self.mycursor = db.cursor()
            return True
        except:
            # En cas d'erreur retourner false
            return False
    '''
        Méthode vérifiant toutes les tables et les crées si elles sont inexistante
    '''
    def checkTable(self):

        warnings.simplefilter("ignore")
        try:
            self.mycursor.execute("CREATE TABLE IF NOT EXISTS `HL9Al4cVYQ`.`category` ( `id` INT NOT NULL AUTO_INCREMENT , `name` VARCHAR(25) NOT NULL , PRIMARY KEY (`id`), UNIQUE `UNIQUE` (`name`)) ENGINE = InnoDB;")
        except Exception as e:
            print('Une erreur "category" ' + e)

        try:
            self.mycursor.execute("CREATE TABLE IF NOT EXISTS `HL9Al4cVYQ`.`user` ( `id` INT NOT NULL AUTO_INCREMENT , `name` VARCHAR(25) NOT NULL , `reg_date` DATE NOT NULL , PRIMARY KEY (`id`), UNIQUE `UNIQUE` (`name`)) ENGINE = InnoDB;")
        except Exception as e:
            print('Une erreur "user" ' + e)

        try:
            self.mycursor.execute("CREATE TABLE IF NOT EXISTS `HL9Al4cVYQ`.`subtitute` ( `id` INT NOT NULL AUTO_INCREMENT , `f_name` VARCHAR(32) NOT NULL , `f_url` VARCHAR(125) NOT NULL , `f_description` TINYTEXT NOT NULL , `reg_date` DATE NULL , `mod_date` DATE NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;")
        except Exception as e:
            print('Une erreur "subtitute" ' + e)

    '''
        Méthode pour extraitre la liste des catégories
    '''
    def extractcat(self):
        self.checkTable()
        sql = "SELECT * FROM category"
        try:
           self.mycursor.execute(sql)
           results = self.mycursor.fetchall()
           for row in results:
              print(row)
        except Exception as e:
           print (e)


    def showdb(self):
        results = self.mycursor.execute("SHOW TABLES")
        print(results)

    '''
        Executé une requête select simple et retouner un dictionnaire
    '''
    def executeselect(self, sql):
        returns = {}
        try:
            results = self.mycursor.execute(sql)
            print(results)
        except Exception as e:
            return print(e)