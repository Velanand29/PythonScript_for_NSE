import datetime
from jugaad_data.nse import bhavcopy_save 
from jugaad_data.nse import bhavcopy_fo_save 
from datetime import datetime  as dt
from datetime import date as da 
import time as t 

#This one is use to get data and store that in the variable "d"
d= datetime.datetime.now() 
#print(CurrentDate.CurrentDate)
#print(CurrentDate.strftime("%A"))
CurrentYear = d.year  # This get the current year and store in the variable current year
CurrentDate = d.date
CurrentMonth = d.month

P_Date = d.date-1
P_Month = d.month-1
P_Year = d.year-1

bhavcopy_fo_save(da(CurrentYear,CurrentMonth,CurrentDate),r"C:\Users\anand\OneDrive\Documents\BHAV COPY")














# # Get the current date and time
# current_datetime = datetime.datetime.now()
# current_da=da.date.now()
# bhavcopy_fo_save(da(2023,4,24),r"C:\Users\anand\OneDrive\Documents\BHAV COPY")
# print(current_da)






# #bhavcopy_fo_save(date(current_datetime),r"C:\Users\anand\OneDrive\Documents\BHAV COPY")
# #print (da)


# # Get yesterday's date
# #yesterday_date = current_datetime - datetime.timedelta(days=1)

# # Check if yesterday is Saturday or Sunday
# #if yesterday_date.weekday() in (5, 6):
#     #yesterday_date = yesterday_date - datetime.timedelta(days=1)
#    # bhavcopy_fo_save(date(2023,4,25),r"C:\Users\anand\OneDrive\Documents\Bhav Copy")

# #GET 
# #bhavcopy_save(date(2023,4,24),r"C:\Users\anand\OneDrive\Documents\Bhav Copy")






