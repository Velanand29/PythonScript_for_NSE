import tkinter as tk
from tkinter import filedialog
import pandas as pd
import json
import sqlite3
import mysql.connector
import yfinance as yf
import datetime
from pymongo import MongoClient



def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        root.destroy()  # Close the pop-up window
        process_file(file_path)

def process_file(csv_file):
    data = pd.read_csv(csv_file)

    save_option = choose_save_option()
    if save_option == "mysql":
        save_to_mysql(data)
    elif save_option == "mongodb":
        save_to_mongodb(data)
    elif save_option == "json":
        save_to_json(data)
    elif save_option == "dataframe":
        create_data_frame(data)
    else:
        print("Invalid option selected.")
        
     # Extracting year, month, week, and stock from 'EXPIRY_DT' column
    data['EXPIRY_YEAR'] = pd.to_datetime(data['EXPIRY_DT']).dt.year
    data['EXPIRY_MONTH'] = pd.to_datetime(data['EXPIRY_DT']).dt.month
    data['EXPIRY_WEEK'] = pd.to_datetime(data['EXPIRY_DT']).dt.isocalendar().week

    # Grouping by 'EXPIRY_YEAR', 'EXPIRY_MONTH', 'EXPIRY_WEEK', and 'INSTRUMENT'
    grouped = data.groupby(['EXPIRY_YEAR', 'EXPIRY_MONTH', 'EXPIRY_WEEK', 'INSTRUMENT'])
    for (year, month, week, instrument), group in grouped:
        print(f"Group: Year: {year} - Month: {month} - Week: {week} - Instrument: {instrument}")
        print(group)
        print()                       
                
def choose_save_option():
    save_options = ["mysql", "mongodb", "json", "dataframe"]
    save_choice = input("Choose where to save the data (mysql/mongodb/json/dataframe): ").lower()
    while save_choice not in save_options:
        print("Invalid option. Please choose from mysql, mongodb, json, or dataframe.")
        save_choice = input("Choose where to save the data (mysql/mongodb/json/dataframe): ").lower()
    return save_choice

def save_to_mysql(data):
    mysql_config = {
        'user': 'your_mysql_username',
        'password': 'your_mysql_password',
        'host': 'localhost',
        'database': 'your_mysql_database',
        'auth_plugin': 'mysql_native_password'
    }
    mysql_conn = mysql.connector.connect(**mysql_config)
    mysql_cursor = mysql_conn.cursor()

    create_table_query = '''
        CREATE TABLE IF NOT EXISTS data (
            INSTRUMENT TEXT,
            SYMBOL TEXT,
            EXPIRY_DT TEXT,
            STRIKE_PR REAL,
            OPTION_TYP TEXT,
            OPEN REAL,
            HIGH REAL,
            LOW REAL,
            CLOSE REAL,
            SETTLE_PR REAL,
            CONTRACTS INTEGER,
            VAL_INLAKH REAL,
            OPEN_INT INTEGER,
            CHG_IN_OI INTEGER,
            TIMESTAMP TEXT
        )
    '''
    mysql_cursor.execute(create_table_query)

    for record in data.to_dict(orient='records'):
        insert_query = '''
            INSERT INTO data (
                INSTRUMENT, SYMBOL, EXPIRY_DT, STRIKE_PR, OPTION_TYP, OPEN,
                HIGH, LOW, CLOSE, SETTLE_PR, CONTRACTS, VAL_INLAKH, OPEN_INT,
                CHG_IN_OI, TIMESTAMP
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        mysql_cursor.execute(insert_query, (
            record['INSTRUMENT'], record['SYMBOL'], record['EXPIRY_DT'],
            record['STRIKE_PR'], record['OPTION_TYP'], record['OPEN'],
            record['HIGH'], record['LOW'], record['CLOSE'], record['SETTLE_PR'],
            record['CONTRACTS'], record['VAL_INLAKH'], record['OPEN_INT'],
            record['CHG_IN_OI'], record['TIMESTAMP']
        ))

    mysql_conn.commit()
    mysql_cursor.close()
    mysql_conn.close()
    print("CSV data stored in MySQL.")

def save_to_mongodb(data):
    mongo_client = MongoClient('mongodb://localhost:27017/')
    mongo_db = mongo_client['your_mongodb_database']
    mongo_collection = mongo_db['data']

    records = data.to_dict(orient='records')
    mongo_collection.insert_many(records)
    mongo_client.close()

    print("CSV data stored in MongoDB.")

def save_to_json(data):
    json_file = input("Enter the JSON file name to save: ")
    if not json_file.endswith(".json"):
        json_file += ".json"

    data_json = data.to_json(orient='records')
    with open(json_file, 'w') as f:
        f.write(data_json)

    print("CSV data saved as JSON.")

def create_data_frame(data):
    print("Displaying DataFrame:")
    print(data)

# Create the main application window
root = tk.Tk()
root.title("CSV to Databases Converter")

# Create a button to open the file dialog
open_button = tk.Button(root, text="Open CSV File", command=open_file_dialog)
open_button.pack(padx=20, pady=10)

# Start the main loop
root.mainloop()
