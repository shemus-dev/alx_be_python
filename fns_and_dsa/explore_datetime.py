from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format and print in "YYYY-MM-DD HH:MM:SS"
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

def calculate_future_date(days_to_add):
    # Get the current date
    current_date = datetime.now()
    # Add the specified number of days
    future_date = current_date + timedelta(days=days_to_add)
    # Format and print in "YYYY-MM-DD"
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date

def main():
    # Part 1: Display current date and time
    display_current_datetime()

    # Part 2: Calculate a future date
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
