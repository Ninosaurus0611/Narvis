import os
from datetime import datetime

PROJECTS_DIR = os.path.join("data", "projects")

def list_projects():
    """Geeft een lijst van beschikbare project-ids terug."""
    if not os.path.exists(PROJECTS_DIR):
        return []
    return [name for name in os.listdir(PROJECTS_DIR)
            if os.path.isdir(os.path.join(PROJECTS_DIR, name))]

def add_note_to_project(project_id: str, text: str):
    """Voegt een notitie toe aan notes.md van een project."""
    project_path = os.path.join(PROJECTS_DIR, project_id)
    notes_path = os.path.join(project_path, "notes.md")

    if not os.path.exists(notes_path):
        raise FileNotFoundError("Project of notes.md bestaat niet.")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    with open(notes_path, "a", encoding="utf-8") as f:
        f.write(f"\n## {timestamp}\n{text.strip()}\n")
