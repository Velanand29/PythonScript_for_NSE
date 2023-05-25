import pandas as pd
import datetime
import urllib.request
import tkinter as tk
from tkinter import filedialog
from datetime import date
from datetime import timedelta
from requests.exceptions import ReadTimeout
from jugaad_data.nse import bhavcopy_save, bhavcopy_fo_save, bhavcopy_fo_raw, bhavcopy_index_raw, bhavcopy_index_save, bhavcopy_raw, full_bhavcopy_raw, full_bhavcopy_save

def download_bhavcopy(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() < 5:  # Skip Saturdays and Sundays
            while True:
                try:
                    bhavcopy_fo_save(current_date, r"C:\Users\anand\OneDrive\Documents\BHAV COPY")
                    break  # Break out of the retry loop if download is successful
                except (ValueError, ReadTimeout):
                    print(f"No data available for {current_date}. Retrying...")
        current_date += timedelta(days=1)

choice = int(input("Enter your choice:\n1. Download using the current date\n2. Enter a specific date\n3. Download data for a specific number of days\n4. Download data within a specific date range\n"))

if choice == 1:
    x = datetime.datetime.now()
    bhavcopy_fo_save(date(int(x.year), int(x.month), int(x.day)), r"C:\Users\anand\OneDrive\Documents\BHAV COPY")
elif choice == 2:
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
            bhavcopy_fo_save(date(y, m, d), r"C:\Users\anand\OneDrive\Documents\BHAV COPY")
elif choice == 3:
    num_days = int(input("Enter the number of days to download the bhavcopy: "))
    download_bhavcopy(num_days)
elif choice == 4:
    valid_start_date = False
    while not valid_start_date:
        start_year = input("Enter the start Year (YYYY): ")
        if not start_year.isdigit() or len(start_year) != 4:
            print("Invalid year format! Please enter a 4-digit year (YYYY).")
            continue
        start_month = input("Enter the start Month (MM): ")
        if not start_month.isdigit() or len(start_month) != 2:
            print("Invalid month format! Please enter a 2-digit month (MM).")
            continue
        start_day = input("Enter the start Day (DD): ")
        if not start_day.isdigit() or len(start_day) != 2:
            print("Invalid day format! Please enter a 2-digit day (DD).")
            continue
        
        start_year = int(start_year)
        start_month = int(start_month)
        start_day = int(start_day)
        
        current_date = datetime.datetime.now().date()
        if start_year > current_date.year or (start_year == current_date.year and start_month > current_date.month) or (start_year == current_date.year and start_month == current_date.month and start_day > current_date.day):
            print("Invalid start date! Start date should not be greater than current date.")
        elif start_month > 12 or start_day > 31:
            print("Invalid date! Day should not be greater than 31 and month should not be greater than 12.")
        else:
            valid_start_date = True
    
    valid_end_date = False
    while not valid_end_date:
        end_year = input("Enter the end Year (YYYY): ")
        if not end_year.isdigit() or len(end_year) != 4:
            print("Invalid year format! Please enter a 4-digit year (YYYY).")
            continue
        end_month = input("Enter the end Month (MM): ")
        if not end_month.isdigit() or len(end_month) != 2:
            print("Invalid month format! Please enter a 2-digit month (MM).")
            continue
        end_day = input("Enter the end Day (DD): ")
        if not end_day.isdigit() or len(end_day) != 2:
            print("Invalid day format! Please enter a 2-digit day (DD).")
            continue
        
        end_year = int(end_year)
        end_month = int(end_month)
        end_day = int(end_day)
        
        current_date = datetime.datetime.now().date()
        if end_year > current_date.year or (end_year == current_date.year and end_month > current_date.month) or (end_year == current_date.year and end_month == current_date.month and end_day > current_date.day):
            print("Invalid end date! End date should not be greater than current date.")
        elif end_month > 12 or end_day > 31:
            print("Invalid date! Day should not be greater than 31 and month should not be greater than 12.")
        else:
            valid_end_date = True
    
    start_date = date(start_year, start_month, start_day)
    end_date = date(end_year, end_month, end_day)
    download_bhavcopy(start_date, end_date)
else:
    print("Invalid choice! Please enter 1, 2, 3, or 4.")
