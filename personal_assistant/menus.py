from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter

from personal_assistant.commands import (
    add_address,
    add_bd,
    add_contact,
    add_email,
    add_note,
    birthdays_num_days,
    change_address,
    change_contact,
    change_email,
    del_contact,
    delete_address,
    delete_email,
    edit_note,
    exit_assistant,
    find_contact,
    num_records,
    remove_note,
    remove_number,
    search_note,
    show_address,
    show_all,
    show_birthday,
    show_email,
    show_notes,
    show_phone,
)
from personal_assistant.src import messages
from personal_assistant.utils.utils import parser

contacts_commands = [
    "add",
    "delete",
    "remove",
    "find",
    "all",
    "num-contacts",
    "show-phone",
    "change-phone",
    "delete-phone",
    "remove-phone",
    "add-birthday",
    "show-birthday",
    "birthdays",
    "add-email",
    "change-email",
    "show-email",
    "delete-email",
    "add-address",
    "change-address",
    "show-address",
    "delete-address",
    "back",
    "return",
    "help",
    "-",
    "exit",
    "close",
]


def contacts_menu():
    print(contacts_interface_title)
    while True:

        commands_completer = WordCompleter(contacts_commands)
        session = PromptSession(completer=commands_completer)
        user_input = session.prompt(
            "\nHow can I help you?\nEnter a command: contacts: "
        )
        command, *args, message = parser(user_input)

        if command in ("exit", "close"):
            exit_assistant()

        if command in ("back", "return", "-"):
            return

        elif command == "help":
            print(messages.contacts_help_center)

        elif command == "add-contact":
            print(add_contact(args))

        elif command == "find":
            print(find_contact(args))

        elif command == "all":
            print(show_all())

        elif command == "show-phone":
            print(show_phone(args))

        elif command == "change-phone":
            print(change_contact(args))

        elif command in ["remove-phone", "delete-phone"]:
            print(remove_number(args))

        elif command == "add-birthday":
            print(add_bd(args))

        elif command == "show-birthday":
            print(show_birthday(args))

        elif command == "birthdays":
            print(birthdays_num_days(args))

        elif command in ["delete", "remove"]:
            print(del_contact(args))

        elif command == "num-contacts":
            print(num_records())

        elif command == "add-email":
            print(add_email(args))

        elif command == "change-email":
            print(change_email(args))

        elif command == "show-email":
            print(show_email(args))

        elif command == "delete-email":
            print(delete_email(args))

        elif command == "add-address":
            print(add_address(args))

        elif command == "change-address":
            print(change_address(args))

        elif command == "show-address":
            print(show_address(args))

        elif command == "delete-address":
            print(delete_address(args))

        elif not command:
            ...

        else:
            print("Invalid command. Please try again.")


notes_commands = [
    "add",
    "create",
    "touch",
    "edit",
    "upd",
    "update",
    "change",
    "ch",
    "remove",
    "delete",
    "del",
    "rm",
    "show",
    "all",
    "list",
    "ls",
    "search",
    "seek",
    "find",
    "filter",
    "grep",
    "help" "back",
    "return",
    "-",
    "exit",
    "close",
]


def notes_menu():
    print(notes_interface_title)
    while True:
        commands_completer = WordCompleter(notes_commands)
        session = PromptSession(completer=commands_completer)
        user_input = session.prompt("\nHow can I help you?\nEnter a command: notes: ")
        command, *args, message = parser(user_input)

        if command in ("exit", "close"):
            exit_assistant()

        if command in ("back", "return", "-"):
            return

        elif command == "help":
            print(messages.notes_help_center)

        elif command in ("add", "create", "touch"):
            print(add_note())

        elif command in ("edit", "upd", "update", "change", "ch"):
            print(edit_note())

        elif command in ("remove", "delete", "del", "rm"):
            print(remove_note())

        elif command in ("show", "all", "list", "ls"):
            print(show_notes())

        elif command in ("search", "seek", "find", "filter", "grep"):
            print(search_note())

        elif not command:
            ...

        else:
            print("Invalid command. Please try again.")
