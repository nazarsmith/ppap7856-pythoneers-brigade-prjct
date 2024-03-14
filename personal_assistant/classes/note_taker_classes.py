from collections import UserDict


class Note:
    def __init__(self, name="Untitled Note", tags=[], text=None):
        self.name = name
        self.tags = tags
        self.text = text

    def __str__(self):
        return f"{self.name}, {self.tags}, {self.text}"


class NoteBook(UserDict):
    def __init__(self):
        super().__init__()

    def add_note(self):
        name = input("Enter note name: ")
        tags = input("Enter note tags (comma-separated): ").split(",")
        text = input("Enter note text: ")

        note = Note(name.strip(), [tag.strip() for tag in tags], text.strip())
        self.data[name] = note
        print("Note added successfully.")

    def get_all_notes(self):
        all_notes = []
        for note in self.data.values():
            all_notes.append(str(note))
        return all_notes

    def remove_note(self, name):
        deleted = self.data.pop(name, None)
        if deleted:
            print(f"Note '{name}' removed successfully.")
        else:
            print(f"Note '{name}' not found in the notebook.")

    def edit_note(self, name, new_text):
        if name in self.data:
            self.data[name].text = new_text
            print(f"Note '{name}' edited successfully.")
        else:
            print(f"Note '{name}' not found in the notebook.")

    def search_note(self, query: str):
        name = query.split("name=")[-1].split(";")[0]
        tag = query.split("tag=")[-1].split(";")[0]
        text = query.split("text=")[-1].split(";")[0]

        def name_matches(note: Note):
            return note.name == name if name else True

        def tag_matches(note: Note):
            return tag in note.tags if tag else True

        def text_matches(note: Note):
            return text in note.text if text else True

        def matches(note):
            return name_matches(note) or tag_matches(note) or text_matches(note)

        matching_notes = list(filter(matches, self.data.values()))

        return matching_notes
