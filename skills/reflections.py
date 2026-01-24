import os
from datetime import datetime
from config.settings import ENABLE_GLOBAL_DECISIONS_LOG

PROJECTS_DIR = os.path.join("data", "projects")
GLOBAL_REFLECTIONS_DIR = os.path.join("data", "reflections")
GLOBAL_REFLECTIONS_FILE = os.path.join(GLOBAL_REFLECTIONS_DIR, "reflections.md")

def _ensure_global_reflections_file():
    os.makedirs(GLOBAL_REFLECTIONS_DIR, exist_ok=True)

    if not os.path.exists(GLOBAL_REFLECTIONS_FILE):
        with open(GLOBAL_REFLECTIONS_FILE, "w", encoding="utf-8") as f:
            f.write("# Reflecties (globaal)\n\n")


def _append_reflection(filepath: str, content: str):
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(content)


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

        reflection_block = (
            f"## {timestamp}\n"
            f"**Project:** {project_id}\n"
            f"**Reflectie:** {reflection.strip()}\n"
            f"**Context:** {context.strip()}\n"
            f"**Les / inzicht:** {lesson.strip()}\n\n"
        )

        # 1 Project-specifieke reflecties
        project_reflections_path = os.path.join(project_path, "reflections.md")

        if not os.path.exists(project_reflections_path):
            with open(project_reflections_path, "w", encoding="utf-8") as f:
                f.write("# Reflecties\n\n")

        _append_reflection(project_reflections_path, reflection_block)

        # 2 Globale reflecties
        _ensure_global_reflections_file()
        _append_reflection(GLOBAL_REFLECTIONS_FILE, reflection_block)
