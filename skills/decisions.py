import os
from datetime import datetime
from config.settings import (
    BASE_DATA_DIR,
    ENABLE_GLOBAL_DECISIONS_LOG
)

PROJECTS_DIR = os.path.join(BASE_DATA_DIR, "projects")
GLOBAL_DECISIONS_DIR = os.path.join(BASE_DATA_DIR, "decisions")
GLOBAL_DECISIONS_FILE = os.path.join(GLOBAL_DECISIONS_DIR, "decisions.md")


def _ensure_global_file():
    os.makedirs(GLOBAL_DECISIONS_DIR, exist_ok=True)
    if not os.path.exists(GLOBAL_DECISIONS_FILE):
        with open(GLOBAL_DECISIONS_FILE, "w", encoding="utf-8") as f:
            f.write("# Beslissingen (globaal)\n\n")


def add_decision_to_project(
    project_id: str,
    decision: str,
    reason: str = "",
    alternatives: str = "",
    impact: str = ""
):
    project_path = os.path.join(PROJECTS_DIR, project_id)
    if not os.path.exists(project_path):
        raise FileNotFoundError("Project bestaat niet.")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    block = (
        f"## {timestamp}\n"
        f"**Beslissing:** {decision}\n"
        f"**Waarom:** {reason}\n"
        f"**Alternatieven:** {alternatives}\n"
        f"**Impact:** {impact}\n\n"
    )

    project_file = os.path.join(project_path, "decisions.md")
    if not os.path.exists(project_file):
        with open(project_file, "w", encoding="utf-8") as f:
            f.write("# Beslissingen\n\n")

    with open(project_file, "a", encoding="utf-8") as f:
        f.write(block)

    if ENABLE_GLOBAL_DECISIONS_LOG:
        _ensure_global_file()
        with open(GLOBAL_DECISIONS_FILE, "a", encoding="utf-8") as f:
            f.write(f"**Project:** {project_id}\n{block}")
