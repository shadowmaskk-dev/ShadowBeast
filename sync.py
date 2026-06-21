import os
import json
import requests

from config import get_groq_key

UNKNOWN_FILE = "database/unknown_topics.json"
GENERAL_FOLDER = "database/general"


def sync_database():

    if not os.path.exists(UNKNOWN_FILE):
        print("No learning queue found.")
        return

    try:
        with open(
            UNKNOWN_FILE,
            "r",
            encoding="utf-8"
        ) as f:
            topics = json.load(f)

    except Exception as e:
        print(
            f"Failed to load learning queue: {e}"
        )
        return

    if not topics:
        print("No pending topics.")
        return

    api_key = get_groq_key()

    if not api_key:
        print("Groq API key not set.")
        return

    remaining = []

    for item in topics:

        topic = item.get(
            "topic",
            ""
        ).strip()

        if not topic:
            continue

        print(
            f"Learning: {topic}"
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
            "messages": [
                {
                    "role": "system",
                    "content": """
Create a concise educational note.

Include:
- Definition
- Explanation
- Examples
- Important points

Plain text only.
"""
                },
                {
                    "role": "user",
                    "content":
                        f"Explain {topic}"
                }
            ]
        }

        try:

            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=120
            )

            response.raise_for_status()

            answer = response.json()[
                "choices"
            ][0][
                "message"
            ][
                "content"
            ]

            filename = (
                topic.lower()
                .replace(" ", "_")
                .replace("/", "_")
            )

            os.makedirs(
                GENERAL_FOLDER,
                exist_ok=True
            )

            filepath = os.path.join(
                GENERAL_FOLDER,
                f"{filename}.txt"
            )

            with open(
                filepath,
                "w",
                encoding="utf-8"
            ) as f:
                f.write(answer)

            print(
                f"Saved: {filepath}"
            )

        except Exception as e:

            print(
                f"Failed: {topic}"
            )

            print(e)

            remaining.append(item)

    try:
        with open(
            UNKNOWN_FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                remaining,
                f,
                indent=4
            )

    except Exception as e:
        print(
            f"Failed to update queue: {e}"
        )

    print(
        "\nSync complete."
    )


if __name__ == "__main__":
    sync_database()

