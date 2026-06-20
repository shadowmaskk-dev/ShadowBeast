import subprocess

from ui import (
    show_banner
)

from plugins.dashboard_plugin import (
    show_dashboard
)

from plugins.loader import (
    load_plugins,
    handle_plugin
)

from ai import (
    ai_chat,
    reset_chat,
    conversation
)

from gemini import (
    gemini_chat
)

AI_PREFIXES = (
    "ai ",
    "shadow ",
    "beast ",
    "shadowbeast ",
    "sb "
)

# Startup

show_banner()

load_plugins()

show_dashboard()

# Main Loop

while True:

    try:

        command = input(
            "\nShadowBeast > "
        ).strip()

        if not command:
            continue

        lower = command.lower()

        # Exit

        if lower == "exit":

            print(
                "Goodbye."
            )

            break

        # Help

        if lower == "help":

            print("""

==============================
       SHADOWBEAST HELP
==============================

[ AI ]

  ai <prompt>
  shadow <prompt>
  beast <prompt>
  shadowbeast <prompt>
  sb <prompt>
  gemini <prompt>

------------------------------

[ CONVERSATION ]

  memory
  reset

------------------------------

[ DASHBOARD ]

  dashboard

------------------------------

[ KNOWLEDGE ]

  kb <topic>
  sync

  remember <text>
  recall <keyword>
  memories

------------------------------

[ PLUGINS ]

  plugins
  reload

------------------------------

[ NOTES ]

  note add
  note list
  note read <name>
  note edit <name>
  note delete <name>

------------------------------

[ FILES ]

  ls
  pwd
  cd <path>
  tree
  mkdir <name>
  rm <name>
  edit <file>

------------------------------

[ CODE RUNNER ]

  run <file.py>

------------------------------

[ BACKUP ]

  backup
  backups
  restore <backup>

------------------------------

[ SYSTEM ]

  battery
  storage
  device
  time
  date

------------------------------

[ API CONFIG ]

  set groq <api_key>
  set gemini <api_key>
  apikeys

------------------------------

[ GENERAL ]

  help
  exit

==============================
Version : 1.0.0
==============================

""")

            continue

        # Memory Count

        if lower == "memory":

            print(
                f"Stored messages: "
                f"{len(conversation)}"
            )

            continue

        # Reset Conversation

        if lower == "reset":

            reset_chat()

            print(
                "Conversation reset."
            )

            continue

        # Gemini Commands

        if lower == "gemini":

            print(
                "Usage: gemini <prompt>"
            )

            continue

        if lower.startswith(
            "gemini "
        ):

            prompt = command[
                8:
            ].strip()

            if not prompt:

                print(
                    "Empty Gemini prompt."
                )

                continue

            print(
                "\nThinking...\n"
            )

            reply = gemini_chat(
                prompt
            )

            print(
                reply
            )

            continue

        # AI Commands

        ai_used = False

        for prefix in AI_PREFIXES:

            if lower.startswith(
                prefix
            ):

                prompt = command[
                    len(prefix):
                ].strip()

                if not prompt:

                    print(
                        "Empty AI prompt."
                    )

                    ai_used = True
                    break

                print(
                    "\nThinking...\n"
                )

                reply = ai_chat(
                    prompt
                )

                print(
                    reply
                )

                ai_used = True

                break

        if ai_used:
            continue

        # Plugins

        handled = handle_plugin(
            command
        )

        if handled:
            continue

        # Shell Fallback

        try:

            result = subprocess.run(
                command,
                shell=True,
                text=True,
                capture_output=True
            )

            output = (
                result.stdout
                if result.stdout
                else result.stderr
            )

            if output:

                print(
                    output.strip()
                )

            else:

                print(
                    "Command executed."
                )

        except Exception as e:

            print(
                f"Shell Error: {e}"
            )

    except KeyboardInterrupt:

        print(
            "\nUse 'exit' to quit."
        )

    except Exception as e:

        print(
            f"Error: {e}"
        )
