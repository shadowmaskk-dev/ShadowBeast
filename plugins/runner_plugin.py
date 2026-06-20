import os
import subprocess

from plugins.file_plugin import (
    current_path
)


def run_file(filename):

    try:

        path = os.path.join(
            current_path,
            filename
        )

        if not os.path.exists(
            path
        ):

            print(
                "File not found."
            )

            return

        ext = os.path.splitext(
            filename
        )[1].lower()

        print(
            "\nRunning...\n"
        )

        if ext == ".py":

            result = subprocess.run(
                [
                    "python",
                    path
                ],
                capture_output=True,
                text=True
            )

        elif ext == ".js":

            result = subprocess.run(
                [
                    "node",
                    path
                ],
                capture_output=True,
                text=True
            )

        elif ext == ".sh":

            result = subprocess.run(
                [
                    "bash",
                    path
                ],
                capture_output=True,
                text=True
            )

        else:

            print(
                "Unsupported file type."
            )

            return

        if result.stdout:

            print(
                result.stdout
            )

        if result.stderr:

            print(
                result.stderr
            )

    except Exception as e:

        print(
            f"Run Error: {e}"
        )


def handle(command):

    lower = command.lower()

    if lower.startswith(
        "run "
    ):

        run_file(
            command[4:].strip()
        )

        return True

    return False
