from config import (
    get_groq_key,
    get_gemini_key,
    set_groq_key,
    set_gemini_key
)


def handle(command):

    lower = command.lower()

    # Set Groq Key

    if lower.startswith(
        "set groq "
    ):

        key = command[
            len("set groq "):
        ].strip()

        if not key:

            print(
                "Usage: set groq <api_key>"
            )

            return True

        set_groq_key(
            key
        )

        print(
            "Groq API key saved."
        )

        return True

    # Set Gemini Key

    if lower.startswith(
        "set gemini "
    ):

        key = command[
            len("set gemini "):
        ].strip()

        if not key:

            print(
                "Usage: set gemini <api_key>"
            )

            return True

        set_gemini_key(
            key
        )

        print(
            "Gemini API key saved."
        )

        return True

    # API Status

    if lower == "apikeys":

        print("""
=========================
API KEY STATUS
=========================
""")

        print(
            "Groq   :",
            "Configured"
            if get_groq_key()
            else "Missing"
        )

        print(
            "Gemini :",
            "Configured"
            if get_gemini_key()
            else "Missing"
        )

        return True

    return False
