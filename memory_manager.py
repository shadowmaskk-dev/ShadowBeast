import os
import json

from context import SYSTEM_PROMPT

MEMORY_FILE = "memory/chat.json"

conversation = []


def load_memory():

    global conversation

    os.makedirs(
        "memory",
        exist_ok=True
    )

    if os.path.exists(
        MEMORY_FILE
    ):

        try:

            with open(
                MEMORY_FILE,
                "r",
                encoding="utf-8"
            ) as f:

                conversation = json.load(f)

        except Exception:

            conversation = [
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                }
            ]

    else:

        conversation = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

        save_memory()

    return conversation


def save_memory():

    os.makedirs(
        "memory",
        exist_ok=True
    )

    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            conversation,
            f,
            indent=2,
            ensure_ascii=False
        )


def reset_memory():

    global conversation

    conversation = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    save_memory()


def add_message(
    role,
    content
):

    global conversation

    conversation.append(
        {
            "role": role,
            "content": content
        }
    )

    # Keep memory size reasonable

    if len(conversation) > 40:

        conversation = (
            conversation[:1]
            +
            conversation[-39:]
        )

    save_memory()


def get_conversation():

    global conversation

    if not conversation:

        load_memory()

    return conversation


# Automatically load memory
load_memory()
