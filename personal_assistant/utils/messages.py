contacts_menu = """
Usage: 

    "ADDRESS_BOOK" COMMAND [OPTIONS]...

Commands:
    add                <name> <phone>   # add a new contact to your list.
    delete/remove      <name>   # delete the contact from your list.
    find               <name>   # search the contact from your list.
    entries            # show the count of contacts in your list.
    all                # show all contacts

    show-phone         <name>   # show the phone number(s) of the contact.
    change-phone       <name> <old_phone> <new_phone>   # change the phone number(s) for the contact.
    delete-phone       <name> <phone>   # delete the phone number from the contact.

    add-address        <name> <address>   # add the address to the contact.
    show-address       <name>   # show the address of the contact.
    change-address     <name> <new_address>   # change the address of the contact.
    delete-address     <name> # delete the address of the contact.

    add-email          <name> <email>   #add an email to the contact.
    show-email         <name>   # show the email of the contact.
    change-email       <name> <old_email> <new_email>   #change the email of the contact.
    delete-email       <name> <email>   #delete the email of the contact.

    add-birthday       <name> <DD.MM.YYYY>   # add the birthday of the contact.
    change-birthday    <name> <old_birthday> <new_birthday>   # change the birthday of the contact.
    show-birthday      <name>   # show the birthday of the contact.
    delete-birthday    <name>   # delete the birthday of the contact.
    birthdays          <count_of_days>   # show contacts that have their birthday within next N days

    back               # back to prev menu
"""

notes_menu = """
Usage: 

    "NOTES_BOOK" COMMAND [OPTIONS]...

Commands:
    add          <text>   # create a new note.
    show         <note_number>   # show the note by the number of note.
    change       <note_number> <new_text>   # change the content of a specific note.
    delete       <note_number>   # delete the note from your notes.
    all          # show all notes
	find         <text>   # show all notes that contain the keyword. 
    back         # back to prev menu
"""
