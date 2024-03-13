import pickle

from personal_assistant import _CACHE_DIR
from personal_assistant.classes.address_book_classes import AddressBook
from personal_assistant.classes.note_taker_classes import NoteBook


class PersonalAssistant(AddressBook, NoteBook):

    def __init__(self):

        super().__init__()
        NoteBook.__init__(self)
        self._load_cache_data()

    def cache_data(self):
        with open(_CACHE_DIR.joinpath("book.bin"), "wb") as file:
            pickle.dump(self, file)

    def _load_cache_data(self):
        cache_file = _CACHE_DIR.joinpath("book.bin")

        if cache_file.exists():
            with open(_CACHE_DIR.joinpath("book.bin"), "rb") as file:
                cache = pickle.load(file)
                self.data.update(cache)
