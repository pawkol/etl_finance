import mysql.connector
from config import DB_CONFIG
from config import currency


def tableCreation():
    connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor()

    for x in currency:

        cursor.execute(
            f"""CREATE TABLE IF NOT EXISTS currency_data_{x}
            (
                id AUTO_INCREMENT PRIMARY KEY INT,
                date DATE,
                hour TIME,
                exchange_rate FLOAT
            )
            """
            )
        
    cursor.close()
    connection.close()


if __name__ == "__main__":
    tableCreation()