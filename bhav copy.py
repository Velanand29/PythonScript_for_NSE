import pandas as pd
import datetime
import urllib.request
import tkinter as tk
from tkinter import filedialog
from datetime import date
from datetime import time 
from jugaad_data.nse import bhavcopy_save, bhavcopy_fo_save, bhavcopy_fo_raw, bhavcopy_index_raw, bhavcopy_index_save, bhavcopy_raw, full_bhavcopy_raw, full_bhavcopy_save

choice = int(input("Enter 1 to download using the current date or 2 to enter a specific date: "))

if choice == 1:
    # Download bhavcopy for futures and options
    # Format (YYYY,M,DD)
    # Do Not use 2023-08-02, use 2023-5-9
    # Download Using current Date 
    x = datetime.datetime.now()
    bhavcopy_fo_save(date(int(x.year), int(x.month), int(x.day)), r"C:\Users\anand\OneDrive\Documents\BHAV COPY")
elif choice == 2:
    y = int(input("Enter the Year: "))
    m = int(input("Enter the Month: "))
    d = int(input("Enter the Day: "))
    bhavcopy_fo_save(date(y, m, d), r"C:\Users\anand\OneDrive\Documents\BHAV COPY")
else:
    print("Invalid choice! Please enter 1 or 2.")
