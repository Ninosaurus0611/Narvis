import os
from datetime import datetime
from config.settings import BASE_DATA_DIR

PROJECTS_DIR = os.path.join(BASE_DATA_DIR, "projects")


def add_note_to_project(project_id: str, text: str):
    project_path = os.path.join(PROJECTS_DIR, project_id)
    notes_path = os.path.join(project_path, "notes.md")

    if not os.path.exists(notes_path):
        raise FileNotFoundError("notes.md niet gevonden.")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    with open(notes_path, "a", encoding="utf-8") as f:
        f.write(f"\n## {timestamp}\n{text.strip()}\n")


def list_projects() -> list[str]:
    """Geeft een lijst van project-id’s terug."""
    if not os.path.exists(PROJECTS_DIR):
        return []
    return sorted(
        name for name in os.listdir(PROJECTS_DIR)
        if os.path.isdir(os.path.join(PROJECTS_DIR, name))
    )
