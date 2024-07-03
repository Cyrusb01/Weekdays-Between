from exceptions import InvalidDate, InvalidInput


def tomohiko_sakamoto_algo(month: int, day: int, year: int) -> int:
    """
    Given the date, this algorithm will return the day of the week.
    Sunday 0 - Saturday 6

    Things to consider:
    - relies on a lookup table for months instead of their given value
    - Jan and Feb should be counted as the previous year.
    """

    month_lookup_table = {
        1: 0,
        2: 3,
        3: 2,
        4: 5,
        5: 0,
        6: 3,
        7: 5,
        8: 1,
        9: 4,
        10: 6,
        11: 2,
        12: 4,
    }
    if month <= 2:
        year -= 1  # Watch out for calculating year 0?

    day_of_week = (
        year + year // 4 - year // 100 + year // 400 + month_lookup_table[month] + day
    ) % 7
    return day_of_week


def count_leap_years_since(year: int):
    return year // 4 - year // 100 + year // 400


def get_days_in_full_years(start_year, end_year):
    num_full_years = end_year - start_year - 1
    # Instead lets calculate how many leap years are in between the two years
    leap_years_before_start = count_leap_years_since(start_year)
    leap_years_before_end = count_leap_years_since(end_year - 1)
    leap_years_in_between = leap_years_before_end - leap_years_before_start
    days = 365 * num_full_years + leap_years_in_between
    return days


def is_leap_year(year: int) -> bool:
    divisible_by_4 = year % 4 == 0
    end_of_century = year % 100 == 0
    divisible_by_400 = year % 400 == 0

    if end_of_century:
        return divisible_by_400
    else:
        return divisible_by_4


def get_days_in_month(year: int, month: int) -> int:
    if month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        return 31


def get_num_days_between_dates(
    *,
    start_year: int,
    start_month: int,
    start_day: int,
    end_year: int,
    end_month: int,
    end_day: int,
) -> int:
    days = 0

    if start_year == end_year:
        if start_month == end_month:
            days += end_day - start_day + 1
        else:
            # Days in full months
            for month in range(start_month + 1, end_month):
                days += get_days_in_month(start_year, month)

            # Days in partial months
            days += get_days_in_month(start_year, start_month) - start_day + 1
            days += end_day

    else:
        days += get_days_in_full_years(start_year, end_year)
        # Full months until end of start year
        for month in range(start_month + 1, 13):
            days += get_days_in_month(start_year, month)

        # Full months until end month in end year
        for month in range(1, end_month):
            days += get_days_in_month(end_year, month)

        # Days in partial months
        days += get_days_in_month(start_year, start_month) - start_day + 1
        days += end_day

    return days


def convert_date_to_ints(date: str) -> tuple:
    # split by / or -
    if "/" in date:
        split_char = "/"
    elif "-" in date:
        split_char = "-"
    else:
        raise InvalidInput

    split_date = date.split(split_char)
    if len(split_date) != 3:
        raise InvalidInput

    try:
        split_date = [int(x) for x in split_date]
    except:
        raise InvalidInput

    month, day, year = split_date[0], split_date[1], split_date[2]

    if not validate_date(month=month, day=day, year=year):
        raise InvalidDate

    return (day, month, year)


def validate_date(month: int, day: int, year: int):
    if year < 1:
        return False
    elif month < 1 or month > 12:
        return False

    days_in_month = get_days_in_month(year=year, month=month)
    if day < 1 or day > days_in_month:
        return False

    return True


def get_weekdays_between(start_date: str, end_date: str):
    # Convert date to int format
    start_day, start_month, start_year = convert_date_to_ints(start_date)
    end_day, end_month, end_year = convert_date_to_ints(end_date)
    print(f"{start_date}-{end_date}")

    if (end_year - start_year) > 20_000_000:
        print("Interesting Input... This might take a while")

    # Check that start date > end date
    if end_year < start_year:
        raise InvalidInput("End date is earlier than start date")
    if end_year == start_year and end_month < start_month:
        raise InvalidInput("End date is earlier than start date")
    if end_year == start_year and end_month == start_month and end_day < start_day:
        raise InvalidInput("End date is earlier than start date")

    # First find out how many days are in between the two dates
    num_days_in_between = get_num_days_between_dates(
        start_year=start_year,
        start_month=start_month,
        start_day=start_day,
        end_year=end_year,
        end_month=end_month,
        end_day=end_day,
    )

    # For each full week between the dates we know there will be 5 weekdays
    num_weeks_in_between = num_days_in_between // 7
    weekdays_in_between = num_weeks_in_between * 5

    """
    In order to determine the leftover weekdays we use the tomohiko sakamoto algorithm 
    This algorithm determines the day of the week given the date.

    Once we know the weekday we start on, and how many days are not part of a full week. 
    We iterate through the remaining days to find how many weekdays are left
    """
    start_weekday = tomohiko_sakamoto_algo(
        year=start_year, month=start_month, day=start_day
    )
    weekday_lookup = {0: 0, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 0}
    left_over_days = num_days_in_between % 7
    curr_day = start_weekday
    for _ in range(left_over_days):
        if curr_day > 6:
            curr_day = 0
        weekdays_in_between += weekday_lookup[curr_day]
        curr_day += 1

    return weekdays_in_between
