import pandas as pd
import datetime
import urllib.request
import tkinter as tk
from tkinter import filedialog
from datetime import date
from datetime import timedelta
from jugaad_data.nse import bhavcopy_save, bhavcopy_fo_save, bhavcopy_fo_raw, bhavcopy_index_raw, bhavcopy_index_save, bhavcopy_raw, full_bhavcopy_raw, full_bhavcopy_save

def download_bhavcopy(num_days):
    end_date = datetime.datetime.now().date()
    start_date = end_date - timedelta(days=num_days - 1)
    
    current_date = start_date
    while current_date <= end_date:
        bhavcopy_fo_save(current_date, r"C:\Users\anand\OneDrive\Documents\BHAV COPY")
        current_date += timedelta(days=1)

choice = int(input("Enter 1 to download using the current date,***2 to enter a specific date, or 3 to download data for a specific number of days: "))

if choice == 1:
    x = datetime.datetime.now()
    bhavcopy_fo_save(date(int(x.year), int(x.month), int(x.day)), r"C:\Users\anand\OneDrive\Documents\BHAV COPY")
elif choice == 2:
    y = int(input("Enter the Year: "))
    m = int(input("Enter the Month: "))
    d = int(input("Enter the Day: "))
    bhavcopy_fo_save(date(y, m, d), r"C:\Users\anand\OneDrive\Documents\BHAV COPY")
elif choice == 3:
    num_days = int(input("Enter the number of days to download the bhavcopy: "))
    download_bhavcopy(num_days)
else:
    print("Invalid choice! Please enter 1, 2, or 3.")
