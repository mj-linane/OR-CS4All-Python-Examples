# Birthday Countdown Tracker
"""
- Keep a list of people and their birthdays
- Calculate days until their birthdays
- Report to me a list of birthdays
"""

import datetime

people = {
    "JONAH": {"year": 2000, "month": 12, "day": 19},
    "TESS": {"year": 2003, "month": 5, "day": 5},
    "ADAM": {"year": 2003, "month": 5, "day": 8},
}

# TODO: MOVE DATE ACCESS TO GLOBAL
# Add this year
now = datetime.datetime.today()
yr = now.year
month = now.month
day = now.day


def get_days_until_bday(name):
    # Convert to date object
    birthday = datetime.date(
        yr, people[name]['month'], people[name]['day'])

    # Format today's date for comparision
    today_date = datetime.date(yr, month, day)

    # Calculate difference in days
    difference = birthday - today_date

    return int(difference.days)


def report_person_days_left(name):
    # Here we can assign a variable to the returned value of a function
    num_days = get_days_until_bday(name)

    # Check for difference
    if num_days == 0:
        return (
                name.capitalize()
                + "'s birthday is today!"
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


def report_person_age_turning(name):
    # TODO: CREATE AGE TURNING FUNCTION

    num_days = get_days_until_bday(people[name])

    # TODO: WRITE OUT CAL HELPER FUNCTION
    def cal_person_age_turning(name):
        if num_days < 0:
            return yr - people[name]['year'] + 1
        else:
            return yr - people[name]['year']

    age = cal_person_age_turning(name)

    # TODO: WRITE OUT RESULTS
    if num_days == 0:
        return (
                name.capitalize() +
                " turns " +
                str(age) +
                " today."
        )
    else:
        return (
                name.capitalize() +
                " is turning " +
                str(age) +
                "."
        )


def report_all_birthdays():
    for name in people:
        print(
            report_person_days_left(name),
            # TODO: Add call to age turning
            report_person_age_turning(name),
        )


report_all_birthdays()
