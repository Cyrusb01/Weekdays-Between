import calendar
import unittest
from datetime import datetime, timedelta

from exceptions import InvalidDate, InvalidInput
from helpers import (convert_date_to_ints, get_days_in_month,
                     get_num_days_between_dates, get_weekdays_between,
                     is_leap_year, tomohiko_sakamoto_algo)


class TestWeekdayFunctions(unittest.TestCase):
    def test_tomohiko_sakamoto_algo(self):
        def _convert_datetime_weekday_to_sakamoto(weekday):
            """
            Convert datetime's weekday to Sakamoto's weekday format.

            Datetime uses monday as 0, Sakamoto uses sunday as 0.
            """
            return (weekday + 1) % 7

        self.assertEqual(
            tomohiko_sakamoto_algo(year=2024, month=5, day=30),
            _convert_datetime_weekday_to_sakamoto(datetime(2024, 5, 30).weekday()),
        )
        self.assertEqual(
            tomohiko_sakamoto_algo(year=2023, month=6, day=1),
            _convert_datetime_weekday_to_sakamoto(datetime(2023, 6, 1).weekday()),
        )
        self.assertEqual(
            tomohiko_sakamoto_algo(year=2000, month=1, day=1),
            _convert_datetime_weekday_to_sakamoto(datetime(2000, 1, 1).weekday()),
        )
        self.assertEqual(
            tomohiko_sakamoto_algo(year=1999, month=12, day=31),
            _convert_datetime_weekday_to_sakamoto(datetime(1999, 12, 31).weekday()),
        )
        # Historical dates
        self.assertEqual(
            tomohiko_sakamoto_algo(year=1776, month=7, day=4),
            _convert_datetime_weekday_to_sakamoto(datetime(1776, 7, 4).weekday()),
        )
        self.assertEqual(
            tomohiko_sakamoto_algo(year=1945, month=5, day=8),
            _convert_datetime_weekday_to_sakamoto(datetime(1945, 5, 8).weekday()),
        )

    def test_is_leap_year(self):
        years = [2020, 2021, 2000, 1900, 1600, 1700]
        for year in years:
            self.assertEqual(is_leap_year(year=year), calendar.isleap(year))

    def test_get_days_in_month(self):
        def _days_in_month(year, month):
            return calendar.monthrange(year, month)[1]

        self.assertEqual(get_days_in_month(year=2024, month=1), _days_in_month(2024, 1))
        self.assertEqual(get_days_in_month(year=2024, month=2), _days_in_month(2024, 2))
        self.assertEqual(get_days_in_month(year=2021, month=2), _days_in_month(2021, 2))
        self.assertEqual(get_days_in_month(year=2021, month=4), _days_in_month(2021, 4))
        self.assertEqual(get_days_in_month(year=2020, month=2), _days_in_month(2020, 2))
        self.assertEqual(get_days_in_month(year=2019, month=2), _days_in_month(2019, 2))

    def test_get_num_days_between_dates(self):
        def _days_between_datetime(
            start_year, start_month, start_day, end_year, end_month, end_day
        ):
            start_date = datetime(start_year, start_month, start_day)
            end_date = datetime(end_year, end_month, end_day)
            return (end_date - start_date).days + 1

        self.assertEqual(
            get_num_days_between_dates(
                start_year=2024,
                start_month=5,
                start_day=30,
                end_year=2024,
                end_month=7,
                end_day=5,
            ),
            _days_between_datetime(2024, 5, 30, 2024, 7, 5),
        )
        self.assertEqual(
            get_num_days_between_dates(
                start_year=2023,
                start_month=1,
                start_day=1,
                end_year=2023,
                end_month=1,
                end_day=31,
            ),
            _days_between_datetime(2023, 1, 1, 2023, 1, 31),
        )
        self.assertEqual(
            get_num_days_between_dates(
                start_year=2020,
                start_month=2,
                start_day=28,
                end_year=2020,
                end_month=3,
                end_day=1,
            ),
            _days_between_datetime(2020, 2, 28, 2020, 3, 1),
        )
        self.assertEqual(
            get_num_days_between_dates(
                start_year=2000,
                start_month=1,
                start_day=1,
                end_year=2001,
                end_month=1,
                end_day=1,
            ),
            _days_between_datetime(2000, 1, 1, 2001, 1, 1),
        )

        self.assertEqual(
            get_num_days_between_dates(
                start_year=2000,
                start_month=1,
                start_day=1,
                end_year=2020,
                end_month=1,
                end_day=1,
            ),
            _days_between_datetime(2000, 1, 1, 2020, 1, 1),
        )
        self.assertEqual(
            get_num_days_between_dates(
                start_year=1900,
                start_month=1,
                start_day=1,
                end_year=2000,
                end_month=1,
                end_day=1,
            ),
            _days_between_datetime(1900, 1, 1, 2000, 1, 1),
        )
        self.assertEqual(
            get_num_days_between_dates(
                start_year=1500,
                start_month=1,
                start_day=1,
                end_year=2000,
                end_month=1,
                end_day=1,
            ),
            _days_between_datetime(1500, 1, 1, 2000, 1, 1),
        )

    def test_get_weekdays_between(self):
        def _calculate_weekdays_between(start_date_str, end_date_str):
            start_date = datetime.strptime(start_date_str, "%m/%d/%Y")
            end_date = datetime.strptime(end_date_str, "%m/%d/%Y")
            weekdays_count = 0
            while start_date <= end_date:
                if start_date.weekday() < 5:
                    weekdays_count += 1
                start_date += timedelta(days=1)
            return weekdays_count

        self.assertEqual(
            get_weekdays_between(start_date="5/30/2024", end_date="7/5/2024"),
            _calculate_weekdays_between("5/30/2024", "7/5/2024"),
        )
        self.assertEqual(
            get_weekdays_between(start_date="1/1/2023", end_date="1/31/2023"),
            _calculate_weekdays_between("1/1/2023", "1/31/2023"),
        )
        self.assertEqual(
            get_weekdays_between(start_date="2/28/2020", end_date="3/1/2020"),
            _calculate_weekdays_between("2/28/2020", "3/1/2020"),
        )
        self.assertEqual(
            get_weekdays_between(start_date="1/1/2000", end_date="1/1/2020"),
            _calculate_weekdays_between("1/1/2000", "1/1/2020"),
        )
        self.assertEqual(
            get_weekdays_between(start_date="1/1/1900", end_date="1/1/2000"),
            _calculate_weekdays_between("1/1/1900", "1/1/2000"),
        )
        self.assertEqual(
            get_weekdays_between(start_date="1/1/0001", end_date="1/1/2000"),
            _calculate_weekdays_between("1/1/0001", "1/1/2000"),
        )
        self.assertEqual(
            get_weekdays_between(start_date="6/28/2024", end_date="6/28/2024"),
            _calculate_weekdays_between("6/28/2024", "6/28/2024"),
        )


# Test Error Handling
class TestExceptionHandling(unittest.TestCase):
    def test_invalid_date(self):
        with self.assertRaises(InvalidDate) as context:
            convert_date_to_ints("02/30/2020")
        self.assertEqual(
            str(context.exception), "Invalid Date. This date does not exist"
        )

    def test_invalid_input_format(self):
        with self.assertRaises(InvalidInput) as context:
            convert_date_to_ints("30 02 2020")
        self.assertEqual(
            str(context.exception),
            "This date format is not supported. use mm/dd/y or mm-dd-y",
        )

    def test_end_date_earlier_than_start_date(self):
        with self.assertRaises(InvalidInput) as context:
            get_weekdays_between("02/01/2020", "01/01/2020")
        self.assertEqual(str(context.exception), "End date is earlier than start date")


if __name__ == "__main__":
    unittest.main()
