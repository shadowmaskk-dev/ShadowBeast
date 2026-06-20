from knowledge import (
    remember,
    recall,
    memory_count
)


def handle(command):

    lower = command.lower()

    if lower.startswith(
        "remember "
    ):

        text = command[
            9:
        ].strip()

        if text:

            remember(
                text
            )

            print(
                "\nMemory saved."
            )

        else:

            print(
                "\nNothing to remember."
            )

        return True

    if lower.startswith(
        "recall "
    ):

        query = command[
            7:
        ].strip()

        results = recall(
            query
        )

        if results:

            print()

            for item in results:

                print(
                    "-",
                    item
                )

        else:

            print(
                "\nNo matching memories."
            )

        return True

    if lower == "memories":

        print(
            f"\nStored Memories: "
            f"{memory_count()}"
        )

        return True

    return False
