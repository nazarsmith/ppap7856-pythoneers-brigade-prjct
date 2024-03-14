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
            print(personal_assistant.notebook.add_note())

        elif command == "remove-note":
            note_name = input("Enter the name of the note to delete: ")
            print(personal_assistant.notebook.remove_note(note_name))

        elif command == "show-notes":
            print(personal_assistant.notebook.get_all_notes())

        elif command == "edit-note":
            note_name = input("Enter the name of the note you want to edit: ")
            new_text = input("Enter the new text for the note: ")
            print(personal_assistant.notebook.edit_note(note_name, new_text))

        elif command == "search-note":
            search_term = input("Enter search query: ")
            print(personal_assistant.notebook.search_note(search_term))

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
