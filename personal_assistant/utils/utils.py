from personal_assistant.src.personal_assistant import personal_assistant


def parser(user_input):
    print(user_input)
    if user_input == "":
        return None, None, "Please start with a valid command."

    command, *args = user_input.split(",")
    if command in ("contacts", "notes", "exit", "close", "help"):
        pass
    else:
        print(type(command))
        command = personal_assistant.classifier.predict(command)
        print(command)
    # command, *args = user_input.split()
    # command = command.lower().strip()
    return command, *args, None
