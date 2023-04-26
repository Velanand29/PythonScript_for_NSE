import requests
import datetime

# Get the current date and time
now = datetime.datetime.now()

# Get the URL of the NIFTY TOTAL MARKET file
url = f"https://www.nseindia.com/market-data/live-equity-market/MW-NIFTY-TOTAL-MARKET-{now.year}-{now.month}-{now.day}.csv"

# Make a request to download the file
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:

    # Create a file object to write the downloaded file to
    with open(f"NIFTY_TOTAL_MARKET_{now.year}-{now.month}-{now.day}.csv", "wb") as f:

        # Write the downloaded file to the file object
        f.write(response.content)

else:

    print("Error downloading file:", response.status_code)
