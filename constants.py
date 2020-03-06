import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="" ,database="projet5")

CATEGORIES = ['Sandwichs',
              'Conserves',
              'Viandes',
              'Plats préparés',
              'Snacks']

quantity = 15