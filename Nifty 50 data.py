import pandas as pd

def read_excel_file(filename):
  """Reads an Excel file and returns a Pandas DataFrame."""
  df = pd.read_excel(filename)
  return df

def print_date_open_high_low_close_adjusted_close(df):
  """Prints the date, open, high, low, close, and adjusted close prices."""
  for index, row in df.iterrows():
    print("Date:", row["Date"])
    print("Open:", row["Open"])
    print("High:", row["High"])
    print("Low:", row["Low"])
    print("Close:", row["Close"])
    print("Adjusted Close:", row["Adj Close"])

if __name__ == "__main__":
  filename = "C:\Users\anand\Downloads\Nifty_50"
  df = read_excel_file(filename)
  print_date_open_high_low_close_adjusted_close(df)
