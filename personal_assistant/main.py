import personal_assistant.utils.messages as messages
from personal_assistant.commands import (
    add_contact,
    show_all,
    change_contact,
    show_phone,
    greeting,
    remove_number,
    add_bd,
    show_birthday,
    birthdays_next_week,
    del_contact,
    num_records,
    add_email,
    change_email,
    delete_email,
    add_address,
    change_address,
    delete_address,
    show_address,
    show_email,
    add_note,
    edit_note,
    show_notes,
    remove_note,
    search_note,
    find_contact,
)
from personal_assistant.src.personal_assistant import personal_assistant
from personal_assistant.src.utils import parser


def main():
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("How can I help you?\nEnter a command: ")
        command, *args, message = parser(user_input)
        if message:
            print(message)

        if command in ["exit", "close"]:
            print("Good bye!")
            personal_assistant.cache_data()
            break

        elif command in ["hello", "hi", "greetings"]:
            print(greeting(), end=" ")

        elif command == "add":
            print(add_contact(args))

        elif command == "find":
            print(find_contact(args))

        elif command == "all":
            print(show_all())

        elif command == "phone":
            print(show_phone(args))

        elif command == "change":
            print(change_contact(args))

        elif command == "remove-phone":
            print(remove_number(args))

        elif command == "add-birthday":
            print(add_bd(args))

        elif command == "show-birthday":
            print(show_birthday(args))

        elif command == "birthdays":
            [print(bd) for bd in birthdays_next_week()]

        elif command in ["delete", "remove"]:
            print(del_contact(args))

        elif command == "entries":
            print(num_records())

        elif command == "help":
            print(messages.contacts_menu + messages.notes_menu)

        elif command == "add-note":
            print(add_note())

        elif command == "edit-note":
            print(edit_note())

        elif command == "remove-note":
            print(remove_note())

        elif command == "show-notes":
            print(show_notes())

        elif command == "search-note":
            print(search_note())

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
            pass

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
