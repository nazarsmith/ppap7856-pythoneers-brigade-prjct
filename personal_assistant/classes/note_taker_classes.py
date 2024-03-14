from collections import UserList


class Note:
    def __init__(self, name, tags, text):
        self.name = name
        self.tags = tags
        self.text = text

    def __str__(self):
        return f"{self.name}, {self.tags}, {self.text}"


class NoteBook(UserList):
    def __init__(self):
        super().__init__()

    def add_note(self):
        name = input("Enter note name: ")
        tags = input("Enter note tags (comma-separated): ").split(",")
        text = input("Enter note text: ")

        note = Note(name.strip(), [tag.strip() for tag in tags], text.strip())
        self.data.append(note)
        return "Note added successfully."

    def get_all_notes(self):
        return 'All Notes:\n' + '\n'.join(str(note) for note in self.data) if self.data else 'No notes found.'

    def remove_note(self, name):
        matching_notes = [note for note in self.data if note.name == name]
        [self.data.remove(note) for note in matching_notes]

        if matching_notes:
            return f"{len(matching_notes)} notes with name '{name}' were removed successfully."
        else:
            return f"Note '{name}' not found in the notebook."

    def edit_note(self, name, new_text):
        matching_notes = [note for note in self.data if note.name == name]

        if matching_notes:
            matching_notes[0].text = new_text
            return f"Note '{name}' edited successfully."
        else:
            return f"Note '{name}' not found in the notebook."

    def search_note(self, query: str):
        name = query.split("name=")[-1].split(';')[0] if 'name=' in query else None
        tag = query.split("tag=")[-1].split(';')[0] if 'tag=' in query else None
        text = query.split("text=")[-1].split(";")[0] if 'text=' in query else None

        def name_matches(note: Note):
            return note.name == name if name else True

        def tag_matches(note: Note):
            return tag in note.tags if tag else True

        def text_matches(note: Note):
            return text in note.text if text else True

        def matches(note):
            return name_matches(note) and tag_matches(note) and text_matches(note)

        matching_notes = list(filter(matches, self.data))

        return 'Matching Notes:\n' + '\n'.join(
            str(n) for n in matching_notes
        ) if matching_notes else 'No matching notes found.'
