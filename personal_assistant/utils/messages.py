add_contact_success = "✅ or 🟢 Contact successfully added"
add_note_success = "✅ or 🟢 Note successfully added"
incorrect_phone_number = "❌ or 🔴 Incorrect phone number"
incorrect_phone_number = "❌ or 🔴 Incorrect phone number"
something_went_wrong = "🔴 Something went wrong. Please try again."


welcome_message = """
=============================================================================================
   / __ \___  ______________  ____  ____ _/ /  /   |  __________(_)____/ /_____ _____  / /_
  / /_/ / _ \/ ___/ ___/ __ \/ __ \/ __ `/ /  / /| | / ___/ ___/ / ___/ __/ __ `/ __ \/ __/
 / ____/  __/ /  (__  ) /_/ / / / / /_/ / /  / ___ |(__  |__  ) (__  ) /_/ /_/ / / / / /_  
/_/    \___/_/  /____/\____/_/ /_/\__,_/_/  /_/  |_/____/____/_/____/\__/\__,_/_/ /_/\__/ "
=============================================================================================
👋👋 Welcome to the assistant bot! 👋👋

Please select one of the menu options:
>> contacts
>> notes
>> exit/close
"""

address_book_interface_title = """
=====================================================================
    ___       __    __                       __                __  
   /   | ____/ /___/ /_______  __________   / /_  ____  ____  / /__
  / /| |/ __  / __  / ___/ _ \/ ___/ ___/  / __ \/ __ \/ __ \/ //_/
 / ___ / /_/ / /_/ / /  /  __(__  |__  )  / /_/ / /_/ / /_/ / ,<   
/_/  |_\__,_/\__,_/_/   \___/____/____/  /_.___/\____/\____/_/|_|  
=====================================================================
👋👋 Welcome to the address book! 👋👋

You can find out the available commands using "help"
"""

notes_book_interface_title = """
=========================================================
    _   __      __               __                __  
   / | / /___  / /____  _____   / /_  ____  ____  / /__
  /  |/ / __ \/ __/ _ \/ ___/  / __ \/ __ \/ __ \/ //_/
 / /|  / /_/ / /_/  __(__  )  / /_/ / /_/ / /_/ / ,<   
/_/ |_/\____/\__/\___/____/  /_.___/\____/\____/_/|_|  
==========================================================
👋👋 Welcome to the notes book! 👋👋

You can find out the available commands using "help"
"""

contacts_help_center = """
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

notes_help_center = """
Usage: 

    "NOTES_BOOK" COMMAND [OPTIONS]...

Commands:
    add          <text>   # create a new note.
    show         <note_number>   # show the note by the number of note.
    change       <note_number> <new_text>   # change the content of a specific note.
    delete       <note_number>   # delete the note from your notes.
    all          # show all notes
    find         tag=<text> or text=<text> or name=<name>  # show all notes that contain the keyword. 

    back         # back to prev menu
"""
