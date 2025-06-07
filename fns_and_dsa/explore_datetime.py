import datetime
# display the current date and time.
def display_current_datetime():
    current_date = datetime.datetime.now()
    print(f"Current date and time: {current_date}")

# Calculate the future date
def calculate_future_date():
    current_date = datetime.date.today()
    days_added = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.timedelta(days=days_added) + current_date
    print(f"Future date: {future_date}")

display_current_datetime()
calculate_future_date()

