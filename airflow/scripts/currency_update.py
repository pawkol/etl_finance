import requests
import mysql.connector
from datetime import datetime
from config import DB_CONFIG
from config import currency


def extract():
    print ("extract")

def transform():
    print ("transform")

def load():
    print ("load")

    connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor()




    cursor.close()
    connection.close()



if __name__=="__main__" :
    print ("hello")
    print (f"{DB_CONFIG["user"]}")