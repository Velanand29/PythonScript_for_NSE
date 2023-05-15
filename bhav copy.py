import datetime
from datetime import date
from datetime import time 
from jugaad_data.nse import bhavcopy_save, bhavcopy_fo_save

#Download bhavcopy for Stocks
#bhavcopy_save(date(2023,3,23), r"C:\Users\anand\OneDrive\Documents\BHAV COPY")

# Download bhavcopy for futures and options
#Format (YYYY,M,DD)
#Do Not use 2023-08-02  use 2023-5-9
print("Enter the Number 1 to get the todays data, Please try after 7.30pm in Indian TimeZone")
print("Enter the date to download F&O Data")
D=input("Enter the Day in the format as D for 1-9 and DD for 10-31 :")
M=input("Enter the Month in the format as M for 1-9 and MM for 10-12 :")
Y=input("Enter the Year in the format as YYYY :")
bhavcopy_fo_save(date(int(Y),int(M),int(D)), r"C:\Users\anand\OneDrive\Documents\BHAV COPY")











# print("Enter the Number to peform the particular operation")
# print("Enter the Number 1 to get the todays data, Please try after 8.30pm in Indian TimeZone")
# print("Enter the Number 2 to give the Date , Moonth , Year""The format should be 'YYYY','MM''DD'")
# print("Enter the Number 3 to get the previous date data")
# Number=input("Enter the given option")

# #if(Number == 1): 
#     # Download bhavcopy on Current date Month and Year 
# current_time = datetime.datetime.now()
     
#   #Download bhavcopy for Stocks
# bhavcopy_save(date(current_time.year,current_time.month,current_time.day), r"C:\Users\anand\OneDrive\Documents\BHAV COPY")
# #Download bhavcopy for futures and options
# bhavcopy_fo_save(date(current_time.year,current_time.month,current_time.day), r"C:\Users\anand\OneDrive\Documents\BHAV COPY")

# #Downlaod Bhavcopy of Yesterday 
# #if (Number ==2 ): 
# current_time = datetime.datetime.now()              
     
# #Download bhavcopy for Stocks
# bhavcopy_save(date(current_time.year-1,current_time.month-1,current_time.day-1), r"C:\Users\anand\OneDrive\Documents\BHAV COPY")

# #Download bhavcopy for futures and options
# bhavcopy_fo_save(date(current_time.year-1,current_time.month-1,current_time.day-1), r"C:\Users\anand\OneDrive\Documents\BHAV COPY")






# # Function to get the Date Month Year from the user 

# def To_get_data(): 
    
#     bhavcopy_save(date(2023,3,23), r"C:\Users\anand\OneDrive\Documents\BHAV COPY")

# # Download bhavcopy for futures and options
# bhavcopy_fo_save(date(2023,3,23), r"C:\Users\anand\OneDrive\Documents\BHAV COPY")

# To_get_data()

# # This  Download stock data to pandas dataframe
# from jugaad_data.nse import stock_df
# df = stock_df(symbol="SBIN", from_date=date(2020,1,1),
#             to_date=date(2020,1,30), series="EQ")