import os
from datetime import datetime

# Absolute pad naar project root
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
INBOX_DIR = os.path.join(PROJECT_ROOT, "data", "inbox")

def ensure_inbox_exists():
    """Zorg dat de inbox-map bestaat."""
    os.makedirs(INBOX_DIR, exist_ok=True)

def add_to_inbox(content: str, project_id: str = None) -> str:
    """
    Slaat tekst op als een nieuw inbox-item.
    Geeft het volledige pad naar het bestand terug.
    """
    ensure_inbox_exists()
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    if project_id:
        project_dir = os.path.join(INBOX_DIR, project_id)
        os.makedirs(project_dir, exist_ok=True)
        filepath = os.path.join(project_dir, f"inbox_{timestamp}.txt")
    else:
        filepath = os.path.join(INBOX_DIR, f"inbox_{timestamp}.txt")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip())

    return filepath

def list_inbox_items(project_id: str = None):
    """Geeft een gesorteerde lijst van inbox-bestanden terug."""
    ensure_inbox_exists()
    target_dir = INBOX_DIR
    if project_id:
        target_dir = os.path.join(INBOX_DIR, project_id)
        os.makedirs(target_dir, exist_ok=True)
    items = [f for f in os.listdir(target_dir) if f.endswith(".txt")]
    items.sort()
    return items

def read_inbox_item(filename: str, project_id: str = None) -> str:
    """Leest de inhoud van een inbox-bestand."""
    target_dir = INBOX_DIR
    if project_id:
        target_dir = os.path.join(INBOX_DIR, project_id)
    filepath = os.path.join(target_dir, filename)
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Inbox-item niet gevonden: {filepath}")
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def move_inbox_to_project(inbox_file: str, project_id: str):
    """
    Verwerkt een inbox-item door het toe te voegen aan de notes.md van het project.
    - inbox_file: volledig pad van het inbox-bestand
    - project_id: ID van het project
    """
    if not os.path.isfile(inbox_file):
        raise FileNotFoundError(f"Inbox-item niet gevonden: {inbox_file}")

    # map naar het bestaande project
    project_dir = os.path.join(PROJECT_ROOT, "data", "projects", project_id)
    notes_path = os.path.join(project_dir, "notes.md")

    if not os.path.exists(notes_path):
        raise FileNotFoundError(f"notes.md voor project '{project_id}' niet gevonden!")

    # inhoud van inbox lezen
    with open(inbox_file, "r", encoding="utf-8") as f:
        content = f.read().strip()

    # timestamp toevoegen
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    # content toevoegen aan notes.md
    with open(notes_path, "a", encoding="utf-8") as f:
        f.write(f"\n## {timestamp}\n{content}\n")

    # verwijder inbox-bestand
    os.remove(inbox_file)

    return notes_path

