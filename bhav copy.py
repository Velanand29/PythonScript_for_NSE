import pandas as pd
import datetime
import urllib.request
import tkinter as tk
from tkinter import filedialog
from datetime import date
from datetime import timedelta
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

# Main program

# User choice input
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
        
elif choice == 3:
    # Download data for a specific number of days
    num_days = int(input("Enter the number of days to download the bhavcopy: "))
    current_date = datetime.datetime.now().date()
    start_date = current_date - timedelta(days=num_days)
    save_function = choose_save_function()
    if save_function:
        download_bhavcopy(start_date, current_date, save_function)
        
elif choice == 4:
    # Download data within a specific date range
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
    save_function = choose_save_function()
    if save_function:
        download_bhavcopy(start_date, end_date, save_function)
        
elif choice == 5:
    # Download data for a custom date range
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
        
        valid_start_date = validate_date(start_year, start_month, start_day)
        if not valid_start_date:
            print("Invalid start date! Please enter a valid date.")
    
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
        
        valid_end_date = validate_date(end_year, end_month, end_day)
        if not valid_end_date:
            print("Invalid end date! Please enter a valid date.")
    
    start_date = date(start_year, start_month, start_day)
    end_date = date(end_year, end_month, end_day)
    save_function = choose_save_function()
    if save_function:
        download_bhavcopy(start_date, end_date, save_function)
        
elif choice == 6:
    # Download data for yesterday
    save_function = choose_save_function()
    if save_function:
        download_bhavcopy_yesterday(save_function)
        
else:
    print("Invalid choice! Please enter a valid number.")

print("Bhavcopy download complete!")
