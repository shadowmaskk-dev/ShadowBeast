import os
import json

DATABASE_DIR = "database"

KNOWLEDGE_FOLDERS = [
    "coding",
    "linux",
    "android",
    "cybersecurity",
    "networking",
    "general"
]

UNKNOWN_FILE = os.path.join(
    DATABASE_DIR,
    "unknown_topics.json"
)


def search_knowledge(query):

    query = query.lower()

    for folder in KNOWLEDGE_FOLDERS:

        folder_path = os.path.join(
            DATABASE_DIR,
            folder
        )

        if not os.path.exists(folder_path):
            continue

        for file in os.listdir(folder_path):

            file_lower = file.lower()

            search_query = (
                query
                .replace(" ", "_")
            )


            if search_query == file_lower.replace(".txt", ""):
                try:

                    with open(
                        os.path.join(
                            folder_path,
                            file
                        ),
                        "r",
                        encoding="utf-8"
                    ) as f:

                        return f.read()

                except Exception:
                    pass

    return None


def add_unknown_topic(topic):

    topic = topic.strip()

    if not topic:
        return

    try:

        with open(
            UNKNOWN_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)

    except Exception:

        data = []

    for item in data:

        if (
            item.get(
                "topic",
                ""
            ).lower()
            ==
            topic.lower()
        ):

            return

    data.append(
        {
            "topic": topic,
            "status": "pending"
        }
    )

    with open(
        UNKNOWN_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4
        )


def knowledge_stats():

    topic_count = 0

    for folder in KNOWLEDGE_FOLDERS:

        folder_path = os.path.join(
            DATABASE_DIR,
            folder
        )

        if os.path.exists(folder_path):

            topic_count += len(
                os.listdir(
                    folder_path
                )
            )

    try:

        with open(
            UNKNOWN_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            pending = len(
                json.load(f)
            )

    except Exception:

        pending = 0

    return {
        "topics": topic_count,
        "pending": pending
    }
