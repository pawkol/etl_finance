import mysql.connector

DB_CONFIG = {
      "host" : "mysql_database",
      "user" : "user1",
      "password" : "user1",
      "database" : "finance_data"
}

currency = {"PLN_to_USD", "PLN_to_EUR", "EUR_to_USD"}

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