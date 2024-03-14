import re
from datetime import datetime

from personal_assistant.src.exceptions.exceptions import WrongDate


class Field:
    def __init__(self, item):
        self.item = item

    def __str__(self):
        return str(self.item)


class Name(Field):
    def __init__(self, name):
        super().__init__(name)
        self.name = name


class Phone(Field):
    def __init__(self, phone: str):
        super().__init__(phone)
        self.phone = re.match("^[0-9]{10}$", phone).group(0)


class Birthday(Field):
    def __init__(self, birthday: str):
        super().__init__(birthday)
        try:
            checked_birthday = re.match(
                "^[0-3]{1}[0-9]{1}\.[0-1]{1}[0-9]{1}\.[0-9]{4}$", birthday
            ).group(0)
        except AttributeError:
            raise WrongDate("The date must be of the DD.MM.YYYY format. Try again.")
        self.birthday = datetime.strptime(checked_birthday, "%d.%m.%Y")
