# ... (other imports and functions remain the same)

# Main program

# User choice input
choice = int(input("Enter your choice:\n0. Download using bhavcopy_fo_save\n1. Download using the current date\n2. Enter a specific date\n3. Download data for a specific number of days\n4. Download data within a specific date range\n5. Download data for a custom date range\n6. Download data for yesterday\n"))

if choice == 0:
    # Download using bhavcopy_fo_save
    x = datetime.datetime.now()
    save_function = bhavcopy_fo_save
    if save_function:
        save_function(date(int(x.year), int(x.month), int(x.day)), r"C:\Users\anand\OneDrive\Documents\BHAV COPY")

elif choice == 1:
    # ... (existing code remains the same)

# ... (existing code remains the same)

elif choice == 0:
    print("Completed")
    
else:
    print("Invalid choice! Please enter a valid number.")

print("Bhavcopy download complete!")
