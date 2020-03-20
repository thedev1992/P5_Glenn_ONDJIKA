import random
import mysql.connector
from database import DbManager
from api import *
from user import *
from function_main import *


db = Category()
db.show_product(5)