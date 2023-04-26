import datetime
from jugaad_data.nse import bhavcopy_save 
from jugaad_data.nse import bhavcopy_fo_save 

from datetime import datetime  as date 

# Get the current date and time
current_datetime = datetime.datetime.now()

# Get yesterday's date
yesterday_date = current_datetime - datetime.timedelta(days=1)

#GET 
#bhavcopy_save(date(2023,4,24),r"C:\Users\anand\OneDrive\Documents\Bhav Copy")
bhavcopy_fo_save(date(2023,4,25),r"C:\Users\anand\OneDrive\Documents\Bhav Copy")




