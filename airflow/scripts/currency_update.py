import requests
import mysql.connector
from datetime import datetime
from config import DB_CONFIG
from config import currency
import json


def extract(api_url, api_key):
    print ("extract")

    params = {
        'app_id': api_key
    }
    response = requests.get(api_url, params=params, verify=False)
    print(f"Response status code: {response.status_code}")
    print(f"Response text: {response.text}")  
    response.raise_for_status()

    return response.json()




def transform(raw_data):

    print("Transforming data...")
    transformed_data = []


    for pair in currency:
        base, target = pair.split("_to_")
        try:
            rate = raw_data['rates'][target] / raw_data['rates'][base]
        except KeyError:
            raise ValueError(f"Nie można znaleźć kursu waluty dla {pair}")
        
        transformed_data.append({
            "pair": pair,
            "rate": rate,
            "date": raw_data["timestamp"]
        })

    return transformed_data



def load(db_config, transformed_data):
    """
    Ładuje dane do bazy danych.
    """
    print("Loading data into database...")
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    for data in transformed_data:
        cursor.execute(
            """
            INSERT INTO currency_data (date, hour, {pair})
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE {pair} = VALUES({pair})
            """.format(pair=data['pair']),
            (
                datetime.fromtimestamp(data['date']).date(),
                datetime.fromtimestamp(data['date']).time(),
                data['rate']
            )
        )

    connection.commit()
    cursor.close()
    connection.close()



def main():

    API_URL = "https://openexchangerates.org/api/latest.json"
    API_KEY = "xxxxxx"     # paste your api key


    try:
        raw_data = extract(API_URL, API_KEY)

        with open('raw_data.json', 'w') as file:
             json.dump(raw_data, file, indent=4)




        finance_data = transform(raw_data)
        load(DB_CONFIG,finance_data)


    except Exception as e:
        print(f"Error: {e}")


if __name__=="__main__" :
    main()
