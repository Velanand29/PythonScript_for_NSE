from jugaad_data.nse import index_df
from datetime import date, timedelta

# Function to fetch index data within a specified date range
def fetch_index_data(symbol, start_date, end_date):
    index_data = index_df(symbol=symbol, from_date=start_date, to_date=end_date)
    return index_data

# Function to display a menu of index symbol choices and get user selection
def select_index_symbol():
    index_symbols = [
        "Nifty Midcap 50",
        "Nifty Fin Service",
        "Nifty 50",
        "Nifty Bank"
    ]
    
    print("Select an index symbol:")
    for idx, symbol in enumerate(index_symbols, start=1):
        print(f"{idx}. {symbol}")
    
    choice = input("Enter the number corresponding to the desired symbol: ")
    choice_idx = int(choice) - 1
    if choice_idx >= 0 and choice_idx < len(index_symbols):
        return index_symbols[choice_idx]
    else:
        print("Invalid choice.")

# Function to display a menu of predefined date range choices and get user selection
def select_date_range():
    print("Select a date range:")
    print("1. Custom Date Range")
    print("2. Yesterday")
    print("3. Last Week")
    print("4. Last Month")
    print("5. Last Year")
    print("6. Last Decade")
    print("7. All Available Data in DB")
    
    choice = input("Enter the number corresponding to the desired date range: ")
    return choice

# Function to get user input for a date in the format YYYY-MM-DD
def userinput_YYYY_MM_DD():
    valid_date = False
    while not valid_date:
        y = input("Enter the Year (YYYY): ")
        if not y.isdigit() or len(y) != 4:
            print("Invalid year format! Please enter a 4-digit year (YYYY).")
            continue
        m = input("Enter the Month (MM): ")
        if not m.isdigit() or len(m) != 2:
            print("Invalid month format! Please enter a 2-digit month (MM).")
            continue
        d = input("Enter the Day (DD): ")
        if not d.isdigit() or len(d) != 2:
            print("Invalid day format! Please enter a 2-digit day (DD).")
            continue
        valid_date = True
        return date(int(y), int(m), int(d))  # Return the validated date

# Main function
def main():
    index_symbol = select_index_symbol()  # Get user's index symbol choice
    date_range_choice = select_date_range()  # Get user's date range choice

    if date_range_choice == "1":  # Custom Date Range
        start_date = userinput_YYYY_MM_DD()
        end_date = userinput_YYYY_MM_DD()
    else:
        end_date = date.today()
        if date_range_choice == "2":  # Yesterday
            start_date = end_date - timedelta(days=1)
        elif date_range_choice == "3":  # Last Week
            start_date = end_date - timedelta(weeks=1)
        elif date_range_choice == "4":  # Last Month
            start_date = end_date.replace(day=1) - timedelta(days=1)
        elif date_range_choice == "5":  # Last Year
            start_date = end_date.replace(year=end_date.year - 1, day=1, month=1)
        elif date_range_choice == "6":  # Last Decade
            start_date = end_date.replace(year=end_date.year - 10)
        else:  # All Available Data in DB
            start_date = date(2000, 1, 1)  # Choose a reasonable start date for available data
    
    index_data = fetch_index_data(index_symbol, start_date, end_date)
    print(index_data)

if __name__ == "__main__":
    main()
