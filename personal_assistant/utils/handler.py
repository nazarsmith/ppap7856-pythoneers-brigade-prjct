import random
from personal_assistant.classes.address_book_classes import (
    AddressBook,
    Record,
)
from personal_assistant.classes.personal_assistance_classes import PersonalAssistant
from personal_assistant.classes.exceptions import (
    WrongInfoException,
    WrongDate,
    WrongAddress,
    WrongEmail,
    NoValue,
)
from personal_assistant.utils.utils import (
    check_args,
    wrong_input_handling,
    get_contact,
    pre_check_addr,
)


def greeting():
    ## select and play a greeting reaction
    prompt = random.choice(["Hello!", "Hi!", "Greetings!"])
    return prompt


@wrong_input_handling
def add_contact(personal_assistant: PersonalAssistant, args):
    check_args(args, WrongInfoException())

    name = args[0]
    phone = args[-1]
    confirm = None

    if name in list(personal_assistant.data.keys()):

        book_entry = personal_assistant.data[name]
        try:
            if book_entry.find_phone(phone):
                return "This phone number is already associated with this contact."
        except:
            pass

        confirm = input("A contact with this name found. Update it? yes / no: ")
        confirm.lower()
        if confirm in ["yes", "1", "affirmative", "y"]:
            book_entry.add_phone(args[-1])
        else:
            return "Canelling contact addition."

    else:
        contact = Record(name)
        contact.add_phone(args[-1])
        personal_assistant.add_record(contact)

    return "Contact added."


@wrong_input_handling
def change_contact(personal_assistant: PersonalAssistant, args):
    check_args(args, ValueError())

    contact = get_contact(personal_assistant, args[0])
    contact.edit_phone(args[1], args[-1])
    return "Contact updated."


@wrong_input_handling
def show_phone(personal_assistant, args):
    check_args(args, NoValue())
    contact = get_contact(personal_assistant, args[0])
    found_phones = contact.list_str_rep(contact.phones)
    found_phones = "; ".join(found_phones)
    return f"{args[0]}'s phone numbers: {found_phones}"


@wrong_input_handling
def show_all(personal_assistant):
    names = list(personal_assistant.keys())
    add_phone_message = 'Enter "add <name> <number>" to add a contact.'
    if not names:
        yield "No contacts found. " + add_phone_message

    for i in range(len(personal_assistant.keys())):
        contact = get_contact(personal_assistant, names[i])
        found_phones = contact.list_str_rep(contact.phones)

        if not found_phones:
            yield "{:>2}. | {:^20}\n".format(i + 1, names[i]) + add_phone_message
            continue

        message = "{:>2}. | {:^20} | {:>10}".format(i + 1, names[i], found_phones[0])

        if len(found_phones) > 1:
            formatted_phones = "".join(
                ["\n{:>39}".format(phone) for phone in found_phones[1:]]
            )
            yield message + formatted_phones
        elif len(found_phones) == 1:
            yield message


@wrong_input_handling
def add_bd(personal_assistant, args):
    check_args(args, WrongDate())
    contact = get_contact(personal_assistant, args[0])
    contact.add_birthday(args[1])
    return "Birthday date added."


@wrong_input_handling
def show_birthday(personal_assistant, args):
    check_args(args, NoValue())
    contact = get_contact(personal_assistant, args[0])
    bd = contact.birthday
    if bd:
        bd = str(bd)
        return f"{args[0]}'s birthday: {bd}"
    return "No associated birthday date found."


@wrong_input_handling
def birthdays_next_week(personal_assistant):
    return personal_assistant.birthdays_per_week()


@wrong_input_handling
def remove_number(personal_assistant, args):
    check_args(args, WrongInfoException())
    contact = get_contact(personal_assistant, args[0])
    contact.remove_phone(args[-1])
    return f"The number was deleted from {args[0]}'s list of phone numbers."


@wrong_input_handling
def del_contact(personal_assistant, args):
    check_args(args, NoValue())
    personal_assistant.delete(args[0])
    return "The contact was deleted."


@wrong_input_handling
def num_records(personal_assistant):
    message = f"The address book has {personal_assistant.records} entries. "
    if not personal_assistant.records:
        return message + 'Enter "add <name> <number>" to add a contact.'
    else:
        return message + 'Type "all" to list all of them.'


@wrong_input_handling
def add_email(personal_assistant, args):
    check_args(args, WrongEmail())
    contact = get_contact(personal_assistant, args[0])
    contact.add_email(args[1])
    return f"Email address {args[1]} added successfully to contact {args[0]}."


@wrong_input_handling
def change_email(personal_assistant, args):
    if len(args) == 2:
        raise NoValue("Please provide a name, and old + new email addresses.")
    else:
        check_args(args, WrongEmail())
    contact = get_contact(personal_assistant, args[0])
    contact.change_email(args[1], args[2])
    return f"Email address updated successfully for contact {args[0]}."


@wrong_input_handling
def show_email(personal_assistant, args):
    check_args(args, NoValue())
    contact = get_contact(personal_assistant, args[0])
    found_emails = contact.list_str_rep(contact.emails)
    if found_emails:
        found_emails = "; ".join(found_emails)
        return f"{args[0]}'s emails: {found_emails}"
    else:
        return "No emails found."


@wrong_input_handling
def delete_email(personal_assistant, args):
    check_args(args, WrongEmail())
    contact = get_contact(personal_assistant, args[0])
    contact.delete_email(args[1])
    return "The email address was deleted."


@wrong_input_handling
def add_address(personal_assistant, args):
    try:
        address = pre_check_addr(args)
        check_args([args[0], address], WrongAddress())
    except IndexError:
        raise WrongAddress("Neither name not address was provided. Try again.")
    contact = personal_assistant.find(args[0])
    contact.add_address(address)
    return f"Address was added successfully to contact {args[0]}."


@wrong_input_handling
def change_address(personal_assistant, args):
    try:
        address = pre_check_addr(args)
        check_args([args[0], address], WrongAddress())
    except IndexError:
        raise WrongAddress("Neither name not address was provided. Try again.")
    contact = get_contact(personal_assistant, args[0])
    contact.change_address(address)
    return f"Address updated successfully for contact {args[0]}."


@wrong_input_handling
def show_address(personal_assistant, args):
    check_args(args, NoValue())
    contact = get_contact(personal_assistant, args[0])
    add = contact.address
    if add:
        add = str(add)
        return f"{args[0]}'s address: {add}"
    return "No associated address found."


@wrong_input_handling
def delete_address(personal_assistant, args=[]):
    if not args:
        raise NoValue("No name was provided. Try again.")
    contact = get_contact(personal_assistant, args[0])
    contact.delete_address()
    return "The address was deleted."
