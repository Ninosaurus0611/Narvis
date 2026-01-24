import os

# Basis paden
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BASE_DATA_DIR = os.path.join(BASE_DIR, "data")

PROJECTS_DIR = os.path.join(BASE_DATA_DIR, "projects")
INBOX_DIR = os.path.join(BASE_DATA_DIR, "inbox")
DECISIONS_DIR = os.path.join(BASE_DATA_DIR, "decisions")
REFLECTIONS_DIR = os.path.join(BASE_DATA_DIR, "reflections")

# Project defaults
DEFAULT_PROJECT_FILES = [
    "notes.md",
    "project.docx"
]

# Logs
ENABLE_GLOBAL_DECISIONS_LOG = True
ENABLE_GLOBAL_REFLECTIONS_LOG = True

# Inbox gedrag
INBOX_AUTO_DELETE_ON_PROCESS = True

# PROMPTS
DECISION_PROMPTS = {
    "reason": True,
    "alternatives": True,
    "impact": True
}

REFLECTION_PROMPTS = {
    "context": True,
    "lesson": True
}

# AI (voor Later)
AI_MODE = "off" # off / assist / reflect / agent
