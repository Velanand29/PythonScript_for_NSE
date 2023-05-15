from datetime import time 
from jugaad_data.nse import bhavcopy_save, bhavcopy_fo_save
from datetime import date

#Download bhavcopy for Stocks
#bhavcopy_save(date(2023,3,23), r"C:\Users\anand\OneDrive\Documents\BHAV COPY")

# Download bhavcopy for futures and options
#Format (YYYY,M,DD)
#Do Not use 2023-08-02  use 2023-5-9
print("Enter the date to download F&O Data")
D=input("Enter the Day in the format as D for 1-9 and DD for 10-31 :")
M=input("Enter the Month in the format as M for 1-9 and MM for 10-12 :")
Y=input("Enter the Year in the format as YYYY :")
bhavcopy_fo_save(date(int(Y),int(M),int(D)), r"C:\Users\anand\OneDrive\Documents\BHAV COPY")