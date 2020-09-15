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
        "day": 15
    },
    "ADAM": {
        "year": 2000,
        "month": 5,
        "day": 7
    },
}


def get_days_until_bday(name):
    # Get today
    now = datetime.datetime.today()
    yr = now.year
    month = now.month
    day = now.day

    # Get Birthday and Convert to Datetime
    birthday = datetime.date(yr, people[name]["month"], people[name]["day"])

    # Format today's date for compile
    today_date = datetime.date(yr, month, day)

    # Calculate difference in days
    difference = birthday - today_date
    return int(difference.days)


def report_days_left(name):
    # Assign a variable to the returned value of the function
    num_days = get_days_until_bday(name)

    # Check for difference
    if num_days == 0:  # If birthday is today
        return (
            name.capitalize() +
            "'s birthday is today!"
        )
    # Past birthdays
    elif num_days < 0:
        num_days = num_days + 365
        return (
            name.capitalize() +
            "'s birthday is in " +
            str(num_days) +
            " days."
        )

    # Future birthdays
    else:
        return (
            name.capitalize() +
            "'s birthday is in " +
            str(num_days) +
            " days."
        )


def report_all_birthdays():
    for name in people:
        print(report_days_left(name))


report_all_birthdays()
