import os
from datetime import datetime
from skills.notes import add_note_to_project
from config.settings import BASE_DATA_DIR

INBOX_DIR = os.path.join(BASE_DATA_DIR, "inbox")


def ensure_inbox_dir():
    os.makedirs(INBOX_DIR, exist_ok=True)


def add_to_inbox(text: str) -> str:
    """
    Slaat tekst op als inbox-item.
    """
    ensure_inbox_dir()

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"inbox_{timestamp}.txt"
    filepath = os.path.join(INBOX_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text.strip())

    return filename


def list_inbox_items() -> list[str]:
    ensure_inbox_dir()
    return sorted(f for f in os.listdir(INBOX_DIR) if f.endswith(".txt"))


def read_inbox_item(filename: str) -> str:
    filepath = os.path.join(INBOX_DIR, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def move_inbox_to_project(filename: str, project_id: str) -> str:
    """
    Verplaatst een inbox-item naar de notes.md van een project en verwijdert het.
    Geeft het pad van de notes.md terug.
    """
    inbox_file = os.path.join(INBOX_DIR, filename)

    if not os.path.isfile(inbox_file):
        raise FileNotFoundError(f"Inbox-item niet gevonden: {inbox_file}")

    with open(inbox_file, "r", encoding="utf-8") as f:
        content = f.read().strip()

    # voeg toe aan notes.md van het project
    add_note_to_project(project_id, content)

    # verwijder het inbox-item
    os.remove(inbox_file)

    project_notes_path = os.path.join(BASE_DATA_DIR, "projects", project_id, "notes.md")
    return project_notes_path



def delete_inbox_item(filename: str):
    filepath = os.path.join(INBOX_DIR, filename)
    if os.path.exists(filepath):
        os.remove(filepath)
