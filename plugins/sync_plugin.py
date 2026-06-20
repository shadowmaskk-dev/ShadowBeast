from sync import (
    sync_database
)


def handle(command):

    lower = command.lower()

    if lower == "sync":

        sync_database()

        return True

    return False
