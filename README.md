# goitneo-python-hw-3-group-3

## Description
A CLI organizer that can help store contacts' phone numbers and birthday dates.


## Get Started

Run `pip install nsta_assistant` to install the package and then `get-started` to get started. The list of available commands is as follows:

- `hi` or `hello` or `greeting` - to say hi to your favorite PA!
- `add name phone` - to add a acontact and its phone number;
- `all` - to list all the contacts and their phone numbers;
- `phone name` - to list all the phone numbers associated with the contact; 
- `change name old phone new phone` - to change the phone number;
- `remove-phone name phone` - to remove the phone number;
- `add-birthday name DD.MM.YYYY` - to add birthday;
- `show-birthday name` - to show birthday associate with the contact;
- `birthdays` - to show the list of contacts who have a birthday within the following 7 days;
- `delete name` or `remove name` - to delete the contact;
- `entries` - to show the number of contacts
- `close` or `exit` - to exit the personal assistant;

## Notes:

1. Currently, it is not possible to add a contact with a name only. Both name and a phone number must be provided;
2. The PA saves the progress upon exiting; this does not apply to the cases when it is forcefully shut down (e.g. keyboard interrupt)