import os
import json
from datetime import datetime

PROJECTS_DIR = os.path.join("data", "projects")

def ensure_projects_dir():
    os.makedirs(PROJECTS_DIR, exist_ok=True)

def create_project(name: str, description: str = "", goal: str = "", files: list[str] = None) -> str:
    """
    Maakt een nieuw project aan.
    files: lijst van bestanden die aangemaakt moeten worden, bijv. ['notes.md', 'project.json', 'script.py']
    """
    ensure_projects_dir()
    project_id = name.lower().replace(" ", "_")
    project_path = os.path.join(PROJECTS_DIR, project_id)

    if os.path.exists(project_path):
        raise FileExistsError(f"Project '{name}' bestaat al.")

    os.makedirs(project_path)

    # Standaard bestanden
    if files is None:
        files = ["notes.md", "project.docx"]

    for file in files:
        file_path = os.path.join(project_path, file)
        if file.endswith(".md"):
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f"# {name}\n\n")
        elif file.endswith(".json"):
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump({
                    "id": project_id,
                    "name": name,
                    "description": description,
                    "goal": goal,
                    "status": "active",
                    "created_at": datetime.now().isoformat()
                }, f, indent=2)
        elif file.endswith(".py"):
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f"# {name} - Python script\n\n")
        elif file.endswith(".xlsx"):
            # lege Excel placeholder (later openpyxl)
            with open(file_path, "wb") as _:
                pass
        elif file.endswith(".docx"):
            # lege Word placeholder (later python-docx)
            with open(file_path, "wb") as _:
                pass

    return project_id