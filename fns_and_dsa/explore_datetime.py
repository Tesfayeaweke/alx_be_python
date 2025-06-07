from datetime import datetime ,date, timedelta
# display the current date and time.
def display_current_datetime():
    current_date = datetime.now()
    print(f"Current date and time: {current_date}")

# Calculate the future date
def calculate_future_date():
    current_date = date.today()
    days_added = int(input("Enter the number of days to add to the current date: "))
    future_date = timedelta(days=days_added) + current_date
    print(f"Future date: {future_date}")

display_current_datetime()
calculate_future_date()

