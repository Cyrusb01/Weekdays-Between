# Weekday Calculation

This project determines the number of weekdays inclusive between two dates. This is all done using raw python with no external libraries.

## Project Structure

- **exceptions.py**: Custom exceptions for invalid dates and unsupported date formats.
- **helpers.py**: Helper functions for date validation, leap year calculation, and converting dates.
- **main.py**: Main logic for calculating weekdays between two dates
- **testing.py**: Unit tests to verify functionality and exception handling.

## How to Use

### 1. Running the Main Script

After running the script the user will be prompted to enter the dates they want to check

```bash
python main.py
```
## Logic Behind System

The first step is determining how many days are in between the two dates. This is done using calculations on how many days are in a specific month and accounts for leap years.

Once the number of days is found out, we can take this number and divide by 7 to determine how many full weeks lie in between. We know there are 5 weekdays in every full week so we can use this number to get a start on how many weekdays there are.

The last part is the difficult part: finding the lefover weekdays. This relies on the Tomohiko Sakamoto algorithm where we can determine what day of the week it is, given the date. 

By knowing the day of the week of the start date and how many weekdays are not part of a full week, we can determine the leftover weekdays.
