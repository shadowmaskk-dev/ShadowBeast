import os
import zipfile
import shutil
from datetime import datetime

BACKUP_FOLDER = (
    "/storage/emulated/0/ShadowBeastBackups"
)


def create_backup():

    try:

        os.makedirs(
            BACKUP_FOLDER,
            exist_ok=True
        )

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        backup_file = os.path.join(
            BACKUP_FOLDER,
            f"backup_{timestamp}.zip"
        )

        with zipfile.ZipFile(
            backup_file,
            "w",
            zipfile.ZIP_DEFLATED
        ) as zipf:

            files = [

                "main.py",
                "ai.py",
                "database.py",
                "knowledge.py",
                "sync.py",
                "utilities.py"

            ]

            for file in files:

                if os.path.exists(
                    file
                ):

                    zipf.write(
                        file
                    )

            folders = [

                "plugins",
                "knowledge",
                "notes"

            ]

            for folder in folders:

                if not os.path.exists(
                    folder
                ):

                    continue

                for root, dirs, files in os.walk(
                    folder
                ):

                    dirs[:] = [

                        d
                        for d in dirs
                        if d != "__pycache__"
                    ]

                    for file in files:

                        path = os.path.join(
                            root,
                            file
                        )

                        zipf.write(
                            path
                        )

        size = os.path.getsize(
            backup_file
        ) / 1024

        print(
            f"\nBackup created:"
        )

        print(
            os.path.basename(
                backup_file
            )
        )

        print(
            f"Size: {size:.1f} KB"
        )

    except Exception as e:

        print(
            f"Backup Error: {e}"
        )


def list_backups():

    try:

        os.makedirs(
            BACKUP_FOLDER,
            exist_ok=True
        )

        backups = sorted(
            os.listdir(
                BACKUP_FOLDER
            )
        )

        if not backups:

            print(
                "No backups found."
            )

            return

        print()

        for backup in backups:

            path = os.path.join(
                BACKUP_FOLDER,
                backup
            )

            size = (
                os.path.getsize(
                    path
                ) / 1024
            )

            print(
                f"{backup} "
                f"({size:.1f} KB)"
            )

    except Exception as e:

        print(
            f"Error: {e}"
        )


def restore_backup(filename):

    try:

        path = os.path.join(
            BACKUP_FOLDER,
            filename
        )

        if not os.path.exists(
            path
        ):

            print(
                "Backup not found."
            )

            return

        shutil.unpack_archive(
            path,
            "."
        )

        print(
            "Backup restored."
        )

    except Exception as e:

        print(
            f"Restore Error: {e}"
        )


def handle(command):

    lower = command.lower().strip()

    if lower == "backup":

        create_backup()

        return True

    if lower == "backups":

        list_backups()

        return True

    if lower.startswith(
        "restore "
    ):

        restore_backup(
            command[8:].strip()
        )

        return True

    return False
