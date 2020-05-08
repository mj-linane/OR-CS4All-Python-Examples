# Birthday Countdown Tracker
import datetime

people = {
    "JONAH": {"year": 2000, "month": 12, "day": 19},
    "TESS": {"year": 2003, "month": 5, "day": 5},
    "ADAM": {"year": 2003, "month": 5, "day": 8},
}

# Add this year
now = datetime.datetime.today()
yr = now.year
month = now.month
day = now.day


def get_days_until_bday(person):
    # Convert to date object
    birthdate = datetime.date(
        yr, people[person]['month'], people[person]['day'])

    # Format today's date for comparision
    today_date = datetime.date(yr, month, day)

    # Calculate difference in days
    difference = birthdate - today_date

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
    num_days = get_days_until_bday(name)

    def cal_person_age_turning(name):
        if num_days < 0:
            return yr - people[name]['year'] + 1
        else:
            return yr - people[name]['year']

    age = cal_person_age_turning(name)

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
            report_person_age_turning(name),
        )


report_all_birthdays()
# TODO: Add main menu function to for add people
# TODO: Finalize Wisher Function
# def get_random_wish():
#     wishes = [
#         "I hope you are having a great birthday",
#         "Happy birthday!",
#         "I hope you enjoy your birthday",
#     ]
#     return random.choice(wishes)
