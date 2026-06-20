import os
import subprocess

current_path = os.getcwd()


def list_files():

    global current_path

    try:

        items = os.listdir(
            current_path
        )

        if not items:

            print(
                "Folder is empty."
            )

            return

        print()

        for item in sorted(items):

            full_path = os.path.join(
                current_path,
                item
            )

            if os.path.isdir(
                full_path
            ):

                print(
                    f"[DIR]  {item}"
                )

            else:

                print(
                    f"[FILE] {item}"
                )

    except Exception as e:

        print(
            f"Error: {e}"
        )


def change_directory(folder):

    global current_path

    try:

        new_path = os.path.abspath(
            os.path.join(
                current_path,
                folder
            )
        )

        if not os.path.isdir(
            new_path
        ):

            print(
                "Folder not found."
            )

            return

        current_path = new_path

        print(
            f"Current Folder:\n{current_path}"
        )

    except Exception as e:

        print(
            f"Error: {e}"
        )


def print_working_directory():

    global current_path

    print(
        current_path
    )


def read_file(filename):

    global current_path

    try:

        path = os.path.join(
            current_path,
            filename
        )

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as f:

            print()

            print(
                f.read()
            )

    except Exception as e:

        print(
            f"Read Error: {e}"
        )


def find_file(name):

    global current_path

    found = False

    for root, dirs, files in os.walk(
        current_path
    ):

        if name in files:

            print(
                os.path.join(
                    root,
                    name
                )
            )

            found = True

    if not found:

        print(
            "File not found."
        )


def print_tree(path, level=0):

    try:

        items = sorted(
            os.listdir(path)
        )

        for item in items:

            full = os.path.join(
                path,
                item
            )

            print(
                "    " * level +
                item
            )

            if os.path.isdir(
                full
            ):

                print_tree(
                    full,
                    level + 1
                )

    except Exception:
        pass


def tree():

    global current_path

    print_tree(
        current_path
    )

def make_directory(name):

    global current_path

    try:

        path = os.path.join(
            current_path,
            name
        )

        os.makedirs(
            path,
            exist_ok=True
        )

        print(
            f"Folder created: {name}"
        )

    except Exception as e:

        print(
            f"Error: {e}"
        )

def create_file(name):

    global current_path

    try:

        path = os.path.join(
            current_path,
            name
        )

        open(
            path,
            "a"
        ).close()

        print(
            f"File created: {name}"
        )

    except Exception as e:

        print(
            f"Error: {e}"
        )

def write_file(name):

    global current_path

    try:

        path = os.path.join(
            current_path,
            name
        )

        print(
            "Enter text."
        )

        print(
            "Type EOF on a line by itself to save."
        )

        lines = []

        while True:

            line = input()

            if line == "EOF":

                break

            lines.append(
                line
            )

        with open(
            path,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(
                "\n".join(lines)
            )

        print(
            f"Saved: {name}"
        )

    except Exception as e:

        print(
            f"Write Error: {e}"
        )

def append_file(name):

    global current_path

    try:

        path = os.path.join(
            current_path,
            name
        )

        print(
            "Enter text."
        )

        print(
            "Type EOF on a line by itself to save."
        )

        lines = []

        while True:

            line = input()

            if line == "EOF":

                break

            lines.append(
                line
            )

        with open(
            path,
            "a",
            encoding="utf-8"
        ) as f:

            f.write(
                "\n"
            )

            f.write(
                "\n".join(lines)
            )

        print(
            f"Updated: {name}"
        )

    except Exception as e:

        print(
            f"Append Error: {e}"
        )

def edit_file(name):

    global current_path

    try:

        path = os.path.join(
            current_path,
            name
        )

        if not os.path.exists(
            path
        ):

            print(
                "File not found."
            )

            return

        subprocess.run(
            [
                "nano",
                path
            ]
        )

    except Exception as e:

        print(
            f"Edit Error: {e}"
        )

def handle(command):

    lower = command.lower()

    if lower == "pwd":

        print_working_directory()

        return True

    if lower == "files":

        list_files()

        return True

    if lower == "tree":

        tree()

        return True

    if lower.startswith(
        "cd "
    ):

        change_directory(
            command[3:].strip()
        )

        return True

    if lower.startswith(
        "read "
    ):

        read_file(
            command[5:].strip()
        )

        return True

    if lower.startswith(
        "find "
    ):

        find_file(
            command[5:].strip()
        )

        return True
    if lower.startswith(
        "mkdir "
    ):

        make_directory(
            command[6:].strip()
        )

        return True


    if lower.startswith(
        "touch "
    ):

        create_file(
            command[6:].strip()
        )

        return True


    if lower.startswith(
        "write "
    ):

        write_file(
            command[6:].strip()
        )

        return True


    if lower.startswith(
        "append "
    ):

        append_file(
            command[7:].strip()
        )

        return True

    if lower.startswith(
        "edit "
    ):

        edit_file(
            command[5:].strip()
        )

        return True
    return False
