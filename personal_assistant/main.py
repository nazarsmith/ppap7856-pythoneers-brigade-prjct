import os
import pathlib

from personal_assistant.classes.personal_assistance_classes import PersonalAssistant
from personal_assistant.utils.handler import (
    add_contact,
    show_all,
    change_contact,
    show_phone,
    add_bd,
    show_birthday,
    birthdays_next_week,
    remove_number,
    del_contact,
    num_records,
    greeting,
)
from personal_assistant.utils.utils import parser

filepath = pathlib.Path(__file__).parent
pa_loc = filepath.joinpath("PersonalAssistant")
try:
    os.makedirs(pa_loc)
except Exception as err:
    pass


def main():
    try:
        personal_assistant = PersonalAssistant().read_from_file(pa_loc)
    except:
        personal_assistant = PersonalAssistant()

    print("Welcome to the assistant bot!")
    while True:

        user_input = input("How can I help you?\nEnter a command: ")
        command, *args, message = parser(user_input)
        if message:
            print(message)

        if command in ["exit", "close"]:
            print("Good bye!")
            personal_assistant.write_to_file(pa_loc)
            break

        elif command in ["hello", "hi", "greetings"]:
            print(greeting(), end=" ")

        elif command == "add":
            print(add_contact(personal_assistant, args))

        elif command == "all":
            [print(c) for c in show_all(personal_assistant)]

        elif command == "phone":
            print(show_phone(personal_assistant, args))

        elif command == "change":
            print(change_contact(personal_assistant, args))

        elif command == "remove-phone":
            print(remove_number(personal_assistant, args))

        elif command == "add-birthday":
            print(add_bd(personal_assistant, args))

        elif command == "show-birthday":
            print(show_birthday(personal_assistant, args))

        elif command == "birthdays":
            [print(bd) for bd in birthdays_next_week(personal_assistant)]

        elif command in ["delete", "remove"]:
            print(del_contact(personal_assistant, args))

        elif command == "entries":
            print(num_records(personal_assistant))

        elif not command:
            pass

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
