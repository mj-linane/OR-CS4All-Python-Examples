# Birthday Wish Automater

import datetime
import random

people = {
    "ADAM": {"year": 2000, "month": 12, "day": 19},
    "MARY": {"year": 2003, "month": 5, "day": 5},
    "JOHN": {"year": 2003, "month": 5, "day": 6},
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

    return int(difference.days)


def report_days_left(person):
    name = person.upper()
    num_days = get_days_until_bday(people[name])

    # Check for difference
    if num_days == 0:
        return (
            name.capitalize()
            + "'s birthday is today"
        )
    elif num_days < 0:
        num_days = num_days + 365
        return (
            name.capitalize()
            + "'s birthday is in "
            + str(num_days)
            + " days."
        )
    else:
        return (
            name.capitalize()
            + "'s birthday is in "
            + str(num_days)
            + " days."
        )


def report_all_birthdays():
    for person in people:
        print(report_days_left(person))


report_all_birthdays()


# TODO: Create function to calculate age for report
# TODO: Add main menu function to allow additional entries into the birthday wisher program

def get_random_wish():
    # TODO: Finalize wish list and incorporate into composition function
    wishes = ["I hope you are having a great birthday", "Happy birthday!"]
    return random.choice(wishes)
