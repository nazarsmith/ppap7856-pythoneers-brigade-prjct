from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter

import personal_assistant.src.messages as messages
from personal_assistant.commands import exit_assistant, greeting
from personal_assistant.menus import contacts_menu, notes_menu
from personal_assistant.utils.utils import parser

menu_commands = [
    "hello",
    "hi",
    "greetings",
    "contacts",
    "notes",
    "help",
    "exit",
    "close",
]


def main():
    print(messages.welcome_message)
    commands_completer = WordCompleter(menu_commands)
    session = PromptSession(completer=commands_completer)

    while True:
        user_input = session.prompt("Enter command: main menu: ")
        command, *args, message = parser(user_input)
        if message:
            print(message)

        if command in ["exit", "close"]:
            exit_assistant()

        elif command in ["hello", "hi", "greetings"]:
            print(greeting(), end=" ")

        elif command == "help":
            print(messages.main_help_center)

        elif command == "contacts":
            contacts_menu()

        elif command == "notes":
            notes_menu()

        elif not command:
            pass

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
