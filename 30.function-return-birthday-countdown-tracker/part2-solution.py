# Birthday Countdown Tracker

import datetime
import random

people = {
    "JONAH": {"year": 2000, "month": 12, "day": 19},
    "TESS": {"year": 2003, "month": 5, "day": 5},
    "ADAM": {"year": 2003, "month": 5, "day": 6},
}


def get_days_until_bday(person):
    # Add this year
    now = datetime.datetime.today()
    yr = now.year
    month = now.month
    day = now.day

    # Convert to date object
    birthdate = datetime.date(
        yr, person["month"], person["day"])

    # Format today's date for comparision
    today_date = datetime.date(yr, month, day)

    # Calculate difference in days
    difference = birthdate - today_date

    # Convert print to return statement and convert to integer
    return int(difference.days)


def report_days_left(person):
    name = person.upper()
    # Here we can assign a variable to the returned value of a function
    num_days = get_days_until_bday(people[name])

    # Check for difference
    if num_days == 0:  # If birthday is today
        return (
            name.capitalize()
            + "'s birthday is today"
        )
    elif num_days < 0:  # If birthday already happened this year
        num_days = num_days + 365
        return (
            name.capitalize()
            + "'s birthday is in "
            + str(num_days)
            + " days."
        )
    else:  # If birthday is in the future
        return (
            name.capitalize()
            + "'s birthday is in "
            + str(num_days)
            + " days."
        )


def report_all_birthdays():
    # Add Loop To Print Off All People And Birthdays
    for person in people:
        print(report_days_left(person))


report_all_birthdays()


# TODO: Create function to calculate age for report
# TODO: Add main menu function to for add people

def get_random_wish():
    # TODO: Finalize wish list and incorporate into composition function
    wishes = ["I hope you are having a great birthday", "Happy birthday!"]
    return random.choice(wishes)
