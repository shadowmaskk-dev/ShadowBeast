import requests

from config import get_groq_key

from database import (
    add_unknown_topic
)

from memory_manager import (
    conversation,
    add_message
)


def ai_chat(prompt):

    api_key = get_groq_key()

    if not api_key:

        return (
            "Groq API key not set.\n"
            "Use: set groq <api_key>"
        )

    add_message(
        "user",
        prompt
    )

    headers = {
        "Authorization":
            f"Bearer {api_key}",
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

        add_message(
            "assistant",
            reply
        )

        return reply

    except Exception as e:

        add_unknown_topic(
            prompt
        )

        return (
            f"Error: {e}\n\n"
            "Topic added to learning queue."
        )
