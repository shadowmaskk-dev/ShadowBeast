import requests

from config import (
    get_gemini_key
)

from context import (
    SYSTEM_PROMPT
)

from memory_manager import (
    conversation,
    add_message
)

MODEL = "gemini-2.5-flash"


def gemini_chat(prompt):

    api_key = get_gemini_key()

    if not api_key:

        return (
            "Gemini API key not set."
        )

    add_message(
        "user",
        prompt
    )

    # Convert shared conversation
    # into Gemini format

    history = []

    for message in conversation:

        role = message.get(
            "role",
            "user"
        )

        text = message.get(
            "content",
            ""
        )

        # Gemini does not support
        # "system" role directly

        if role == "system":

            history.append(
                {
                    "role": "user",
                    "parts": [
                        {
                            "text": text
                        }
                    ]
                }
            )

        elif role == "assistant":

            history.append(
                {
                    "role": "model",
                    "parts": [
                        {
                            "text": text
                        }
                    ]
                }
            )

        else:

            history.append(
                {
                    "role": "user",
                    "parts": [
                        {
                            "text": text
                        }
                    ]
                }
            )

    url = (
        "https://generativelanguage.googleapis.com"
        f"/v1beta/models/{MODEL}:generateContent"
        f"?key={api_key}"
    )

    payload = {
        "contents": history
    }

    try:

        response = requests.post(
            url,
            json=payload,
            timeout=60
        )

        response.raise_for_status()

        data = response.json()

        reply = data[
            "candidates"
        ][0][
            "content"
        ][
            "parts"
        ][0][
            "text"
        ]

        add_message(
            "assistant",
            reply
        )

        return reply

    except Exception as e:

        return (
            f"Gemini Error: {e}"
        )
