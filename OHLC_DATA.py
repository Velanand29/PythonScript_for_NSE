import yfinance as yf
from datetime import date

# Get today's date
today = date.today()

# Fetch Nifty OHLC data
nifty_data = yf.download('^Reliance', start=today, end=today)

print(nifty_data)
