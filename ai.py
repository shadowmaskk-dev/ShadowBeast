import requests
import json
import os

from config import (
    get_groq_key
)

API_KEY = get_groq_key()
from database import (
    add_unknown_topic
)

SYSTEM_PROMPT = """
You are ShadowBeast, an AI assistant running in Termux.

Environment:
- Running inside a terminal.
- Responses are displayed as plain text.

Response Rules:
- Use plain text only.
- Do not use markdown.
- Do not use **bold**.
- Do not use *italic*.
- Do not use headings.
- Keep answers concise.
- Give practical answers.
- For code, provide code and explanation.
- Prefer short paragraphs.
"""

conversation = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]


def save_memory():

    os.makedirs(
        "memory",
        exist_ok=True
    )

    with open(
        "memory/chat.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            conversation,
            f,
            indent=2
        )


def load_memory():

    global conversation

    if os.path.exists(
        "memory/chat.json"
    ):

        try:

            with open(
                "memory/chat.json",
                "r",
                encoding="utf-8"
            ) as f:

                conversation = json.load(f)

        except Exception:

            pass


def reset_chat():

    global conversation

    conversation = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    save_memory()


def ai_chat(prompt):

    global conversation

    conversation.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Keep conversation size reasonable

    if len(conversation) > 40:

        conversation = (
            conversation[:1]
            +
            conversation[-39:]
        )

    headers = {
        "Authorization":
            f"Bearer {GROQ_API_KEY}",
        "Content-Type":
            "application/json"
    }

    payload = {
        "model":
            "llama-3.3-70b-versatile",
        "messages":
            conversation
    }

    try:

        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=60
        )

        response.raise_for_status()

        reply = response.json()[
            "choices"
        ][0][
            "message"
        ][
            "content"
        ]

        conversation.append(
            {
                "role": "assistant",
                "content": reply
            }
        )

        save_memory()

        return reply

    except Exception as e:

        add_unknown_topic(
            prompt
        )

        return (
            f"Error: {e}\n\n"
            "Topic added to learning queue."
        )


load_memory()
