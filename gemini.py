import requests

from config import (
    get_gemini_key
)

MODEL = "gemini-2.5-flash"


def gemini_chat(prompt):

    api_key = get_gemini_key()

    if not api_key:

        return (
            "Gemini API key not set."
        )

    url = (
        "https://generativelanguage.googleapis.com"
        f"/v1beta/models/{MODEL}:generateContent"
        f"?key={api_key}"
    )

    payload = {

        "contents": [

            {
                "parts": [

                    {
                        "text": prompt
                    }

                ]
            }

        ]

    }

    try:

        response = requests.post(
            url,
            json=payload,
            timeout=60
        )

        response.raise_for_status()

        data = response.json()

        return data[
            "candidates"
        ][0][
            "content"
        ][
            "parts"
        ][0][
            "text"
        ]

    except Exception as e:

        return (
            f"Gemini Error: {e}"
        )
