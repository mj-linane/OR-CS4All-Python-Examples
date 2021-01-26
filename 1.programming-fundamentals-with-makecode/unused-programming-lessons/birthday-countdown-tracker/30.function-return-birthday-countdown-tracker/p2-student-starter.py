# Birthday Countdown Tracker
import datetime

"""
- Keep a list of people and their birthdays
- Calculate days until their birthdays
- Report to me a list of birthdays
"""

people = {
    "JONAH": {
        "year": 2000,
        "month": 12,
        "day": 19
    },
    "TESS": {
        "year": 2003,
        "month": 5,
        "day": 6
    },
    "ADAM": {
        "year": 2000,
        "month": 5,
        "day": 7
    },
}


def get_days_until_bday(person):
    # Get today
    now = datetime.datetime.today()
    yr = now.year
    month = now.month
    day = now.day

    # Get Birthday and Convert to Datetime
    birthday = datetime.date(yr, person["month"], person["day"])
    print(now)
    print(birthday)
    # print(type(birthday))

    # Format today's date for compile
    today_date = datetime.date(yr, month, day)

    # Calculate difference in days
    difference = birthday - today_date
    print(difference)


get_days_until_bday(people["TESS"])

# def report_days_left(person):

# def report_all_bdays():
