import os
import pathlib
import pickle

from personal_assistant.src.address_book.address_book import AddressBook
from personal_assistant.src.notebook.notebook import NoteBook

_CACHE_DIR = pathlib.Path(__file__).parent.parent.joinpath('.cache')

os.makedirs(_CACHE_DIR, exist_ok=True)


class PersonalAssistant:

    def __init__(self):
        self._notebook = NoteBook()
        self._address_book = AddressBook()
        self._load_cache_data()

    @property
    def notebook(self):
        return self._notebook

    @property
    def address_book(self):
        return self._address_book

    def cache_data(self):
        with open(_CACHE_DIR.joinpath("notebook.bin"), "wb") as file:
            pickle.dump(self._notebook, file)
        with open(_CACHE_DIR.joinpath("address_book.bin"), "wb") as file:
            pickle.dump(self._address_book, file)

    def _load_cache_data(self):
        notebook_cache = _CACHE_DIR.joinpath("notebook.bin")
        address_book_cache = _CACHE_DIR.joinpath("address_book.bin")

        if notebook_cache.exists():
            with open(notebook_cache, "rb") as file:
                cache = pickle.load(file)
                self._notebook.data.extend(cache)

        if address_book_cache.exists():
            with open(address_book_cache, "rb") as file:
                cache = pickle.load(file)
                self._address_book.data.update(cache)


personal_assistant = PersonalAssistant()
