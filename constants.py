
# import sql connector for databases
import mysql.connector
# object of database connection
db = mysql.connector.connect(host="localhost", user="root", password="" ,database="projet5")
# categories parameters for api requests
CATEGORIES = ['spaghetti',
              'pizza',
              'fromage',

                        ]
# quantity of product asked
quantity = 20



