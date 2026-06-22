import requests

from config import get_groq_key
from database import add_unknown_topic

from memory_manager import (
    conversation,
    add_message,
    save_memory
)

try:
    from context import SYSTEM_PROMPT
except ImportError:
    SYSTEM_PROMPT = (
        "You are ShadowBeast, a powerful AI assistant. "
        "You help with coding, Linux, Termux, Android, "
        "automation, cybersecurity learning, and general tasks."
    )


# ============================================================
# INITIALIZE CONVERSATION
# ============================================================

if not conversation:
    conversation.append({
        "role": "system",
        "content": SYSTEM_PROMPT
    })


# ============================================================
# SETTINGS
# ============================================================

MODEL = "llama-3.3-70b-versatile"

MAX_CONTEXT_MESSAGES = 20


# ============================================================
# CONTEXT MANAGEMENT
# ============================================================

def trim_conversation():
    """
    Keep only the latest messages while preserving
    the system prompt.
    """

    global conversation

    if len(conversation) <= MAX_CONTEXT_MESSAGES:
        return

    system_message = conversation[0]

    recent_messages = conversation[
        -(MAX_CONTEXT_MESSAGES - 1):
    ]

    conversation.clear()

    conversation.append(system_message)

    conversation.extend(recent_messages)


# ============================================================
# RESET CHAT
# ============================================================

def reset_chat():
    """
    Clears conversation history while preserving
    the system prompt.
    """

    global conversation

    conversation.clear()

    conversation.append({
        "role": "system",
        "content": SYSTEM_PROMPT
    })

    save_memory()

    return "Conversation memory reset."


# ============================================================
# GROQ CHAT
# ============================================================

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

    trim_conversation()

    headers = {
        "Authorization":
            f"Bearer {api_key}",
        "Content-Type":
            "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": conversation,
        "temperature": 0.7
    }

    try:

        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=60
        )

        response.raise_for_status()

        data = response.json()

        reply = data[
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

        save_memory()

        return reply

    except Exception as e:

        add_unknown_topic(prompt)

        return (
            f"Error: {e}\n\n"
            "Topic added to learning queue."
        )
