import os
from datetime import datetime
from config.settings import (
    BASE_DATA_DIR,
    ENABLE_GLOBAL_REFLECTIONS_LOG
)

PROJECTS_DIR = os.path.join(BASE_DATA_DIR, "projects")
GLOBAL_REFLECTIONS_DIR = os.path.join(BASE_DATA_DIR, "reflections")
GLOBAL_REFLECTIONS_FILE = os.path.join(GLOBAL_REFLECTIONS_DIR, "reflections.md")


def _ensure_global_file():
    os.makedirs(GLOBAL_REFLECTIONS_DIR, exist_ok=True)
    if not os.path.exists(GLOBAL_REFLECTIONS_FILE):
        with open(GLOBAL_REFLECTIONS_FILE, "w", encoding="utf-8") as f:
            f.write("# Reflecties (globaal)\n\n")


def add_reflection_to_project(
    project_id: str,
    reflection: str,
    context: str = "",
    lesson: str = ""
):
    project_path = os.path.join(PROJECTS_DIR, project_id)
    if not os.path.exists(project_path):
        raise FileNotFoundError("Project bestaat niet.")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    block = (
        f"## {timestamp}\n"
        f"**Reflectie:** {reflection}\n"
        f"**Context:** {context}\n"
        f"**Les:** {lesson}\n\n"
    )

    project_file = os.path.join(project_path, "reflections.md")
    if not os.path.exists(project_file):
        with open(project_file, "w", encoding="utf-8") as f:
            f.write("# Reflecties\n\n")

    with open(project_file, "a", encoding="utf-8") as f:
        f.write(block)

    if ENABLE_GLOBAL_REFLECTIONS_LOG:
        _ensure_global_file()
        with open(GLOBAL_REFLECTIONS_FILE, "a", encoding="utf-8") as f:
            f.write(f"**Project:** {project_id}\n{block}")
