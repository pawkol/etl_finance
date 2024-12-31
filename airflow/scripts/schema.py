import mysql.connector
from config import DB_CONFIG
from config import currency


def tableCreation():
    connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor()


    cursor.execute(
            f"""CREATE TABLE IF NOT EXISTS currency_data
            (
                id INT AUTO_INCREMENT PRIMARY KEY,
                date DATE,
                hour TIME
            )
            """
            )   

    for x in currency:

        try:
            cursor.execute(
                    f"""ALTER TABLE currency_data
                        ADD COLUMN {x} FLOAT
                    """
                    )   
            
        except mysql.connector.Error as err:
            if err.errno == 1060:  
                print(f"Column {x} already exists")
            else:
                print(f"ADDING ERROR COLUMN {x}: {err}")
        

    cursor.close()
    connection.close()


if __name__ == "__main__":
    tableCreation()