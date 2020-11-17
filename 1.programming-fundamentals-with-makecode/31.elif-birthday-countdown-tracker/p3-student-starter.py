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
        "day": 13
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

    # Format today's date for compile
    today_date = datetime.date(yr, month, day)

    # Calculate difference in days
    difference = birthday - today_date
    return int(difference.days)


def report_days_left(person):
    # Assign a variable to the returned value of the function
    num_days = get_days_until_bday(people[person])

    # Check for difference
    if num_days == 0:  # If birthday is today
        return (
                person.capitalize()
                + "'s birthday is today!"
        )


print(report_days_left("TESS"))

# def report_all_bdays():


# def add(x,y):
#   return x + y

# print(add(2,3))
# print(add(3,10))

# def say_name(name):
#   return name

# print(say_name("mj"))
