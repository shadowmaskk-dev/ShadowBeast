from database import (
    search_knowledge,
    add_unknown_topic
)


def handle(command):

    lower = command.lower()

    if lower == "kb":

        print(
            "Usage: kb <topic>"
        )

        return True

    if lower.startswith(
        "kb "
    ):

        topic = command[
            3:
        ].strip()

        result = search_knowledge(
            topic
        )

        if result:

            print(
                "\n[Knowledge Base]\n"
            )

            print(
                result
            )

        else:

            add_unknown_topic(
                topic
            )

            print(
                "\nNo local knowledge found."
            )

            print(
                "Topic added to learning queue."
            )

        return True

    return False
