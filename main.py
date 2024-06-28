from helpers import get_weekdays_between

if __name__ == "__main__":
    start_date = input("Enter start date (mm/dd/yyyy): ")
    end_date = input("Enter end date (mm/dd/yyyy): ")

    weekdays = get_weekdays_between(start_date=start_date, end_date=end_date)
    print(f"Weekdays in between {start_date}-{end_date}: {weekdays}")
