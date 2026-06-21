import json
import os

NOTES_FILE = "notes/notes.json"


def load_notes():

    if not os.path.exists(
        NOTES_FILE
    ):
        return []

    try:

        with open(
            NOTES_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    except Exception:

        return []


def save_notes(notes):

    os.makedirs(
        "notes",
        exist_ok=True
    )

    with open(
        NOTES_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            notes,
            f,
            indent=4
        )


def handle(command):

    lower = command.lower()

    # Add Note

    if lower.startswith(
        "note add "
    ):

        text = command[
            9:
        ].strip()

        if not text:

            print(
                "Empty note."
            )

            return True

        notes = load_notes()

        notes.append(
            text
        )

        save_notes(
            notes
        )

        print(
            "Note saved."
        )

        return True

    # List Notes

    if lower in (
        "notes",
        "note list"
    ):

        notes = load_notes()

        if not notes:

            print(
                "No notes."
            )

            return True

        print()

        for i, note in enumerate(
            notes,
            start=1
        ):

            print(
                f"[{i}] {note}"
            )

        return True

    # Read Note

    if lower.startswith(
        "note read "
    ):

        try:

            index = int(
                command[
                    10:
                ].strip()
            ) - 1

            notes = load_notes()

            if (
                index < 0
                or index >= len(notes)
            ):

                print(
                    "Invalid note."
                )

                return True

            print(
                f"\n[{index + 1}]"
            )

            print(
                notes[index]
            )

        except Exception:

            print(
                "Usage: note read <id>"
            )

        return True

    # Edit Note

    if lower.startswith(
        "note edit "
    ):

        try:

            index = int(
                command[
                    10:
                ].strip()
            ) - 1

            notes = load_notes()

            if (
                index < 0
                or index >= len(notes)
            ):

                print(
                    "Invalid note."
                )

                return True

            print(
                f"Current: {notes[index]}"
            )

            new_text = input(
                "New text: "
            ).strip()

            if not new_text:

                print(
                    "Edit cancelled."
                )

                return True

            notes[index] = new_text

            save_notes(
                notes
            )

            print(
                "Note updated."
            )

        except Exception:

            print(
                "Usage: note edit <id>"
            )

        return True

    # Search Notes

    if lower.startswith(
        "note search "
    ):

        keyword = command[
            13:
        ].strip().lower()

        notes = load_notes()

        found = False

        print()

        for i, note in enumerate(
            notes,
            start=1
        ):

            if keyword in note.lower():

                print(
                    f"[{i}] {note}"
                )

                found = True

        if not found:

            print(
                "No matching notes."
            )

        return True

    # Delete Note

    if lower.startswith(
        "note delete "
    ):

        try:

            index = int(
                command[
                    12:
                ].strip()
            ) - 1

            notes = load_notes()

            if (
                index < 0
                or index >= len(notes)
            ):

                print(
                    "Invalid note."
                )

                return True

            removed = notes.pop(
                index
            )

            save_notes(
                notes
            )

            print(
                f"Deleted: {removed}"
            )

        except Exception:

            print(
                "Usage: note delete <id>"
            )

        return True

    return False
