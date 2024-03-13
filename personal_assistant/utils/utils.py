import collections
from datetime import datetime, timedelta
from typing import List, Dict, Union

from personal_assistant.classes.exceptions import (
    WrongInfoException,
    WrongDate,
    NoValue,
    NoPhones,
)


def wrong_input_handling(function):
    def handling(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except WrongInfoException as err:
            return err
        except WrongDate as err:
            return err.args[0]
        except NoValue as err:
            return err.args[0]
        except NoPhones as err:
            return err.args[0]
        except AttributeError as err:
            return err.args[0]
        except KeyError as err:
            return err.args[0]
        except ValueError as err:
            return err.args[0]
        except TypeError as err:
            return err.args[0]
        except Exception as err:
            return err.args[0]

    return handling


def get_contact(book, name):
    try:
        contact = book.data[name]
        return contact
    except KeyError:
        raise KeyError(f"The contacts book doesn't have a contact named {name}")


def check_args(args, exc: Exception):
    if isinstance(exc, WrongInfoException):
        if len(args) == 1:
            raise WrongInfoException("Please provide both a name and a phone number.")

        elif len(args) < 1:
            raise WrongInfoException(
                "Neither name nor phone number provided. Please try again."
            )

    elif isinstance(exc, WrongDate):
        if len(args) == 1:
            raise WrongDate("Please provide both a name and a date.")

        elif len(args) < 1:
            raise WrongDate("Neither name nor date was provided. Please try again.")

    elif isinstance(exc, NoValue):
        if len(args) != 1:
            raise NoValue("Please provide a contact name.")

    elif isinstance(exc, ValueError):
        if len(args) == 2:
            raise ValueError("Please provide both old and new phone numbers.")

        elif 1 < len(args) < 2:
            raise ValueError(
                "Neither old nor new phone number provided. Please try again."
            )

        elif len(args) <= 1:
            raise ValueError(
                "Please provide an account name, old and new phone numbers."
            )


def parser(user_input):
    if user_input == "":
        return None, None, "Please start with a valid command."

    command, *args = user_input.split()
    command = command.lower().strip()
    return command, *args, None


def get_birthdays_per_n_days(users: List[Dict[str, Union[str, datetime]]], days: int):
    results = collections.defaultdict(list)
    today = datetime.today().date() + timedelta(days=1)

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if delta_days < days:
            if (dow := birthday_this_year.weekday()) >= 5:
                birthday_this_year = birthday_this_year + timedelta(days=(0 - dow + 7) % 7)

            results[birthday_this_year.strftime('%A')].append(name)

    return [f'{dow}: ' + ', '.join(names) for dow, names in results.items()] if results else [
        f'No birthdays within next {days} days']


## test the function
if __name__ == "__main__":
    test_date = datetime.today()

    users = [
        {
            "name": "Bill Gates",
            "birthday": test_date.replace(
                month=test_date.month - 1
            ),  ## BD this year last month
        },
        {
            "name": "Bill States",
            "birthday": test_date.replace(month=12),  ## BD this year end of year
        },
        {
            "name": "Bill Mates",
            "birthday": test_date.replace(day=test_date.day - 1),  ## BD yesterday
        },
        {
            "name": "Bill Rates",
            "birthday": test_date.replace(day=test_date.day + 1),  ## BD tomorrow
        },
        {"name": "Bill Wates", "birthday": test_date},  ## BD today
        {
            "name": "Bill Spades",
            "birthday": test_date.replace(
                day=test_date.day + 6
            ),  ## BD weekend; needs adjusting
        },
        {
            "name": "Bill Dates",
            "birthday": test_date.replace(day=test_date.day + 7),  ## BD in a week
        },
    ]
    print(users[0])
    r = get_birthdays_per_n_days(users, 3)

    print(r)
