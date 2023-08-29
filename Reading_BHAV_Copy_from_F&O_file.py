import pandas as pd
import os
from datetime import date, datetime, timedelta
from requests.exceptions import ReadTimeout
from jugaad_data.nse import bhavcopy_fo_save

# Function to read Bhavcopy F&O data from a CSV file and display it in a DataFrame
def read_bhavcopy_fo_file(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Bhavcopy F&O data:")
        print(df)
    except FileNotFoundError:
        print("File not found!")

# Function to read Bhavcopy F&O data for today and save it to a CSV file
def download_and_read_bhavcopy():
    today = date.today()
    download_dir = r"C:\Users\anand\OneDrive\Documents\BHAV COPY"
    try:
        bhavcopy_data = bhavcopy_fo_save(today, download_dir)
        file_name = f"fo{today.strftime('%d%b%Y')}bhav.csv"
        file_path = os.path.join(download_dir, file_name)
        with open(file_path, 'w') as file:
            file.write(bhavcopy_data)
        print(f"Bhavcopy F&O data for {today} saved at {file_path}")
        read_bhavcopy_fo_file(file_path)
    except (ValueError, ReadTimeout):
        print(f"No data available for {today}.")

# Main program
download_and_read_bhavcopy()
