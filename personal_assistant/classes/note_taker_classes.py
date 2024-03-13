from collections import UserDict
from personal_assistant.classes.base_classes import Field


class Note(Field):
    def __init__(self, name, tags, text):
        super().__init__(name)
        self.name = name
        self.tags = tags
        self.text = text

    def __str__(self):
        return f"{self.name}, {self.tags}, {self.text}"


class NoteBook(UserDict):
    def __init__(self):
        self.notes = {}

    def add_note(self):
        name = input("Enter the note name:")
        tags = input("Enter the note tags:").split(",")
        text = input("Enter the note text:")
        new_note = Note(name, tags, text)
        print({new_note.name: new_note})
        self.notes.update({new_note.name: new_note})

    def show_notes(self):
        for name, note in self.notes.items():
            print(note)
