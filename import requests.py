import requests
import csv

url = 'https://www.nseindia.com/api/historical/indices?index=NIFTY%20100&from=01-01-2022&to=01-01-2023'
response = requests.get(url)

if response.status_code == 200:
  data = response.json()
  with open('nifty_50.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])
    for row in data['data']:
      writer.writerow([row['date'], row['open'], row['high'], row['low'], row['close'], row['volume']])
else:
  print('Error:', response.status_code)