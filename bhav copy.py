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