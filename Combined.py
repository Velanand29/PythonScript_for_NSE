import pandas as pd
import datetime
import urllib.request
import tkinter as tk
from tkinter import filedialog
from datetime import date, timedelta
from requests.exceptions import ReadTimeout
from jugaad_data.nse import (
    bhavcopy_save,
    bhavcopy_fo_save,
    bhavcopy_fo_raw,
    bhavcopy_index_raw,
    bhavcopy_index_save,
    bhavcopy_raw,
    full_bhavcopy_raw,
    full_bhavcopy_save,
)
from pymongo import MongoClient
import mysql.connector

# Function to validate if the entered date is valid
def validate_date(year, month, day):
    try:
        date(int(year), int(month), int(day))
        return True
    except ValueError:
        return False
    # Function to choose the save function based on user input
def choose_save_function():
    save_function = None
    while not save_function:
        function_choice = int(input("Choose the bhavcopy save function:\n1. bhavcopy_save\n2. bhavcopy_fo_save\n3. bhavcopy_fo_raw\n4. bhavcopy_index_raw\n5. bhavcopy_index_save\n6. bhavcopy_raw\n7. full_bhavcopy_raw\n8. full_bhavcopy_save\n9. Download all\n"))
        if function_choice == 1:
            save_function = bhavcopy_save
        elif function_choice == 2:
            save_function = bhavcopy_fo_save
        elif function_choice == 3:
            save_function = bhavcopy_fo_raw
        elif function_choice == 4:
            save_function = bhavcopy_index_raw
        elif function_choice == 5:
            save_function = bhavcopy_index_save
        elif function_choice == 6:
            save_function = bhavcopy_raw
        elif function_choice == 7:
            save_function = full_bhavcopy_raw
        elif function_choice == 8:
            save_function = full_bhavcopy_save
        elif function_choice == 9:
            save_function = [bhavcopy_save, bhavcopy_fo_save, bhavcopy_fo_raw, bhavcopy_index_raw, bhavcopy_index_save, bhavcopy_raw, full_bhavcopy_raw, full_bhavcopy_save]
        else:
            print("Invalid choice! Please enter a valid number.")
    return save_function

# Function to download bhavcopy data within a specific date range
def download_bhavcopy(start_date, end_date, save_function):
    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() < 5:  # Skip Saturdays and Sundays
            while True:
                try:
                    if isinstance(save_function, list):
                        for func in save_function:
                            func(current_date, r"C:\Users\anand\OneDrive\Documents\BHAV COPY")
                    else:
                        save_function(current_date, r"C:\Users\anand\OneDrive\Documents\BHAV COPY")
                    break  # Break out of the retry loop if download is successful
                except (ValueError, ReadTimeout):
                    print(f"No data available for {current_date}. Retrying...")
        current_date += timedelta(days=1)

# Function to download bhavcopy data for yesterday
def download_bhavcopy_yesterday(save_function):
    yesterday = date.today() - timedelta(days=1)
    if yesterday.weekday() < 5:  # Skip Saturdays and Sundays
        while True:
            try:
                if isinstance(save_function, list):
                    for func in save_function:
                        func(yesterday, r"C:\Users\anand\OneDrive\Documents\BHAV COPY")
                else:
                    save_function(yesterday, r"C:\Users\anand\OneDrive\Documents\BHAV COPY")
                break  # Break out of the retry loop if download is successful
            except (ValueError, ReadTimeout):
                print(f"No data available for {yesterday}. Retrying...")

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
    
# Main program
if __name__ == "__main__":
    print("Welcome to NSE Bhavcopy Downloader and CSV Processor!")

    while True:
        try:
            # User choice input for NSE data download
            choice = int(input("Enter your choice:\n1. Download using the current date\n2. Enter a specific date\n3. Download data for a specific number of days\n4. Download data within a specific date range\n5. Download data for a custom date range\n6. Download data for yesterday\n"))

            if choice == 1:
                # Download using the current date
                x = datetime.datetime.now()
                save_function = choose_save_function()
                if save_function:
                    save_function(date(int(x.year), int(x.month), int(x.day)), r"C:\Users\anand\OneDrive\Documents\BHAV COPY")

            elif choice == 2:
                # Enter a specific date
                valid_date = False
                while not valid_date:
                    y = input("Enter the Year (YYYY): ")
                    if not y.isdigit() or len(y) != 4:
                        print("Invalid year format! Please enter a 4-digit year (YYYY).")
                        continue
                    m = input("Enter the Month (MM): ")
                    if not m.isdigit() or len(m) != 2:
                        print("Invalid month format! Please enter a 2-digit month (MM).")
                        continue
                    d = input("Enter the Day (DD): ")
                    if not d.isdigit() or len(d) != 2:
                        print("Invalid day format! Please enter a 2-digit day (DD).")
                        continue

                    y = int(y)
                    m = int(m)
                    d = int(d)

                    current_date = datetime.datetime.now().date()
                    if y > current_date.year or (y == current_date.year and m > current_date.month) or (y == current_date.year and m == current_date.month and d > current_date.day):
                        print("Invalid start date! Start date should not be greater than current date.")
                    elif m > 12 or d > 31:
                        print("Invalid date! Day should not be greater than 31 and month should not be greater than 12.")
                    else:
                        valid_date = True
                        save_function = choose_save_function()
                        if save_function:
                            save_function(date(y, m, d), r"C:\Users\anand\OneDrive\Documents\BHAV COPY")

            # ... (Similar code blocks for other choices)

            elif choice == 6:
                # Download data for yesterday
                save_function = choose_save_function()
                if save_function:
                    download_bhavcopy_yesterday(save_function)

            else:
                print("Invalid choice! Please enter a valid number.")

            print("Bhavcopy download complete!")

            # CSV Data Processing Section

            # Create the main application window
            root = tk.Tk()
            root.title("CSV to Databases Converter")

            def open_files_dialog():
                file_paths = filedialog.askopenfilenames(filetypes=[("CSV Files", "*.csv")])
                if file_paths:
                    root.destroy()  # Close the pop-up window
                    for file_path in file_paths:
                        process_file(file_path)

            # Create a button to open the file dialog for multiple files
            open_button = tk.Button(root, text="Open CSV Files", command=open_files_dialog)
            open_button.pack(padx=20, pady=10)

            # Start the main loop
            root.mainloop()

        except Exception as e:
            print("An error occurred:", e)
            continue