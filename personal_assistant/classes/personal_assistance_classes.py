import pickle
from personal_assistant.classes.address_book_classes import AddressBook
from personal_assistant.classes.note_taker_classes import NoteBook


class PersonalAssistant(AddressBook, NoteBook):

    def __init__(self):
        super().__init__()
        NoteBook.__init__(self)

    def write_to_file(self, pa_path):
        with open(pa_path.joinpath("book.bin"), "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self, pa_path):
        with open(pa_path.joinpath("book.bin"), "rb") as file:
            book = pickle.load(file)
            return book
