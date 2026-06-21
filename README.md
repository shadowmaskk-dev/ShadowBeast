ShadowBeast

ShadowBeast is a modular AI-powered terminal assistant designed for Termux. It combines AI, automation, system tools, file management, and a plugin architecture into a single command-line experience.

---

Features

- Groq AI integration
- Google Gemini integration
- Modular plugin system
- Dashboard interface
- Notes management
- File explorer utilities
- Backup and restore system
- System information commands
- Python code runner
- Knowledge base system
- Shell command execution fallback
- Run from anywhere in Termux

---

Requirements

- Android device
- Termux
- Termux:API app
- Python 3

---

Installation

Clone the repository:

git clone https://github.com/shadowmaskk-dev/ShadowBeast.git

cd ShadowBeast

Install:

bash install.sh

Launch ShadowBeast:

shadowbeast

---

API Configuration

Configure API keys from inside ShadowBeast.

Set Groq API Key

set groq <api_key>

Stores the Groq API key.

Set Gemini API Key

set gemini <api_key>

Stores the Gemini API key.

Check API Status

apikeys

Shows whether API keys are configured.

---

Commands

AI Commands

Groq AI

ai <prompt>
shadow <prompt>
beast <prompt>
shadowbeast <prompt>
sb <prompt>

Send prompts to the Groq model.

Example:

ai explain recursion

---

Gemini AI

gemini <prompt>

Send prompts to Google Gemini.

---

Conversation Commands

View Conversation Memory Count

memory

Displays the number of stored conversation messages.

Reset Conversation

reset

Clears current AI conversation history.

---

Dashboard

Show Dashboard

dashboard

Displays the ShadowBeast dashboard.

---

Knowledge Commands

Search Knowledge Base

kb <topic>

Search local knowledge database.

Sync Knowledge Database

sync

Synchronize the knowledge database.

Save Memory

remember <text>

Store a custom memory.

Recall Memory

recall <keyword>

Search stored memories.

Memory Statistics

memories

Display total stored memories.

---

Notes System

Create Note

note add

Create a new note.

List Notes

note list

Display all notes.

Read Note

note read <name>

Read a saved note.

Edit Note

note edit <name>

Edit an existing note.

Delete Note

note delete <name>

Delete a note.

---

File Management

List Files

ls

List current directory contents.

Current Directory

pwd

Display current working directory.

Change Directory

cd <path>

Change directory.

Directory Tree

tree

Display directory tree.

Create Directory

mkdir <name>

Create a folder.

Remove File or Folder

rm <name>

Delete a file or directory.

Edit File

edit <file>

Open a file for editing.

---

Code Runner

Run Python File

run <file.py>

Execute Python scripts directly.

---

Backup System

Create Backup

backup

Create a project backup.

List Backups

backups

Display available backups.

Restore Backup

restore <backup>

Restore a selected backup.

---

System Commands

Battery Information

battery

Display battery statistics.

Storage Information

storage

Display storage usage.

Device Information

device

Display device information.

Current Time

time

Show current time.

Current Date

date

Show current date.

---

Plugin Commands

List Plugins

plugins

Display loaded plugins.

Reload Plugins

reload

Reload all plugins.

---

General Commands

Help

help

Display help information.

Exit

exit

Close ShadowBeast.

---

Project Structure

ShadowBeast/
├── main.py
├── ai.py
├── gemini.py
├── config.py
├── ui.py
├── install.sh
├── requirements.txt
├── README.md
├── LICENSE
│
├── plugins/
│   ├── __init__.py
│   ├── loader.py
│   ├── dashboard_plugin.py
│   ├── system_plugin.py
│   ├── notes_plugin.py
│   ├── backup_plugin.py
│   ├── file_plugin.py
│   ├── code_runner_plugin.py
│   └── config_plugin.py
│
├── config/
│   ├── groq_key.txt
│   └── gemini_key.txt
│
├── database/
│   └── general/
│
├── notes/
│
├── backups/
│
└── screenshots/

---

Dependencies

Install dependencies:

pip install -r requirements.txt

Current dependencies:

requests

---

Contributing

Contributions, issues, and suggestions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push your branch.
5. Open a Pull Request.

---

License

This project is licensed under the MIT License.

---

Author

ShadowMaskk

GitHub: https://github.com/shadowmaskk-dev

Built with Python, Termux, and a concerning amount of terminal time.
