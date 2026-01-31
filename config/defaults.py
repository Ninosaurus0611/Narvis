import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BASE_DATA_DIR = os.path.join(BASE_DIR, "data")

ENABLE_GLOBAL_DECISIONS_LOG = True
ENABLE_GLOBAL_REFLECTIONS_LOG = True

DECISION_PROMPTS = {
    "reason": True,
    "alternatives": True,
    "impact": True
}

REFLECTION_PROMPTS = {
    "context": True,
    "lesson": True
}

AI_MODE = "off"
