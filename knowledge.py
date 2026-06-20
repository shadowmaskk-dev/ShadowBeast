import json
import os

MEMORY_FILE = "knowledge/memories.json"


def load_memories():

    if not os.path.exists(
        MEMORY_FILE
    ):

        return []

    try:

        with open(
            MEMORY_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    except Exception:

        return []


def save_memories(memories):

    os.makedirs(
        "knowledge",
        exist_ok=True
    )

    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            memories,
            f,
            indent=4
        )


def remember(text):

    memories = load_memories()

    memories.append(
        {
            "memory": text
        }
    )

    save_memories(
        memories
    )


def recall(query):

    memories = load_memories()

    results = []

    query = query.lower()

    for item in memories:

        memory = item[
            "memory"
        ]

        if query in memory.lower():

            results.append(
                memory
            )

    return results


def memory_count():

    return len(
        load_memories()
    )
