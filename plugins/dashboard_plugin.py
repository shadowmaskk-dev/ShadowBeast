from ai import conversation


def show_dashboard():

    print(r"""
╔══════════════════════════════════════╗
║             SHADOWBEAST             ║
╠══════════════════════════════════════╣
║ AI Providers : Groq + Gemini        ║
║ Chat Memory  : {} Messages          ║
║ Plugin System: Active               ║
║ Status       : Online               ║
║ Version      : 1.0.0                ║
╠══════════════════════════════════════╣
║ Quick Commands                      ║
║                                     
║  help       Show help              ║
║  plugins    List plugins           ║
║  memory     Show chat memory       ║
║  notes      Open notes system      ║
║  battery    Show battery status    ║
║  exit       Exit ShadowBeast       ║
╚══════════════════════════════════════╝
""".format(
        len(conversation)
    ))


def handle(command):

    if command.lower() == "dashboard":

        show_dashboard()

        return True

    return False
