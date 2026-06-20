import os

CONFIG_DIR = "config"

GROQ_KEY_FILE = os.path.join(
    CONFIG_DIR,
    "groq_key.txt"
)

GEMINI_KEY_FILE = os.path.join(
    CONFIG_DIR,
    "gemini_key.txt"
)


def load_key(filepath):

    try:

        with open(
            filepath,
            "r"
        ) as f:

            return (
                f.read()
                .strip()
            )

    except FileNotFoundError:

        return None


def save_key(
    filepath,
    key
):

    os.makedirs(
        CONFIG_DIR,
        exist_ok=True
    )

    with open(
        filepath,
        "w"
    ) as f:

        f.write(
            key.strip()
        )


def get_groq_key():

    return load_key(
        GROQ_KEY_FILE
    )


def get_gemini_key():

    return load_key(
        GEMINI_KEY_FILE
    )


def set_groq_key(key):

    save_key(
        GROQ_KEY_FILE,
        key
    )


def set_gemini_key(key):

    save_key(
        GEMINI_KEY_FILE,
        key
    )
