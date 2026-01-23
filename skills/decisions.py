import os
from datetime import datetime

PROJECTS_DIR = os.path.join("data", "projects")
GLOBAL_DECISIONS_DIR = os.path.join("data", "decisions")
GLOBAL_DECISIONS_FILE = os.path.join(GLOBAL_DECISIONS_DIR, "decisions.md")


def _ensure_global_decisions_file():
    os.makedirs(GLOBAL_DECISIONS_DIR, exist_ok=True)

    if not os.path.exists(GLOBAL_DECISIONS_FILE):
        with open(GLOBAL_DECISIONS_FILE, "w", encoding="utf-8") as f:
            f.write("# Beslissingen-log (globaal)\n\n")


def _append_decision(filepath: str, content: str):
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(content)


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

    decision_block = (
        f"## {timestamp}\n"
        f"**Project:** {project_id}\n"
        f"**Beslissing:** {decision.strip()}\n"
        f"**Waarom:** {reason.strip()}\n"
        f"**Alternatieven:** {alternatives.strip()}\n"
        f"**Gevolgen:** {impact.strip()}\n\n"
    )

    # 1️⃣ Project-specifieke beslissingen-log
    project_decisions_path = os.path.join(project_path, "decisions.md")

    if not os.path.exists(project_decisions_path):
        with open(project_decisions_path, "w", encoding="utf-8") as f:
            f.write("# Beslissingen-log\n\n")

    _append_decision(project_decisions_path, decision_block)

    # 2️⃣ Globale beslissingen-log
    _ensure_global_decisions_file()
    _append_decision(GLOBAL_DECISIONS_FILE, decision_block)
