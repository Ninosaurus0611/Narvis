import os
import json
from datetime import datetime
from config.settings import BASE_DATA_DIR

# Projecten map
PROJECTS_DIR = os.path.join(BASE_DATA_DIR, "projects")


def ensure_projects_dir() -> None:
    """
    Zorgt dat de projecten-map bestaat.
    """
    os.makedirs(PROJECTS_DIR, exist_ok=True)


def list_projects() -> list[str]:
    """
    Geeft een lijst terug van alle project-id's.
    """
    ensure_projects_dir()
    return [
        name
        for name in os.listdir(PROJECTS_DIR)
        if os.path.isdir(os.path.join(PROJECTS_DIR, name))
    ]


def create_project(
    name: str,
    description: str = "",
    goal: str = "",
    files: list[str] | None = None
) -> str:
    """
    Maakt een nieuw project aan.

    - Altijd een projectmap
    - Altijd een project.json (metadata)
    - Optioneel extra bestanden (leeg / simpel)
    """

    ensure_projects_dir()

    if not name.strip():
        raise ValueError("Projectnaam mag niet leeg zijn.")

    project_id = name.lower().replace(" ", "_")
    project_path = os.path.join(PROJECTS_DIR, project_id)

    if os.path.exists(project_path):
        raise FileExistsError(f"Project '{project_id}' bestaat al.")

    os.makedirs(project_path)

    # 1️⃣ Metadata (altijd)
    project_data = {
        "id": project_id,
        "name": name,
        "description": description,
        "goal": goal,
        "created_at": datetime.now().isoformat()
    }

    project_json_path = os.path.join(project_path, "project.json")
    with open(project_json_path, "w", encoding="utf-8") as f:
        json.dump(project_data, f, indent=2)

    # 2️⃣ Optionele bestanden (dom, geen slimme logica)
    if files:
        for filename in files:
            file_path = os.path.join(project_path, filename)

            if os.path.exists(file_path):
                continue

            with open(file_path, "w", encoding="utf-8") as f:
                if filename.endswith(".md"):
                    f.write(f"# {name}\n\n")

    return project_id
