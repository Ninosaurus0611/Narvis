from config.defaults import (
    BASE_DATA_DIR,
    DECISION_PROMPTS,
    REFLECTION_PROMPTS,
    ENABLE_GLOBAL_DECISIONS_LOG,
    ENABLE_GLOBAL_REFLECTIONS_LOG,
    AI_MODE,
)

# Hier kun je overrides doen, bijv:
# AI_MODE = "assist"
# ENABLE_GLOBAL_DECISIONS_LOG = False

# klein gebruik
__all__ = [
    "BASE_DATA_DIR",
    "DECISION_PROMPTS",
    "REFLECTION_PROMPTS",
    "ENABLE_GLOBAL_DECISIONS_LOG",
    "ENABLE_GLOBAL_REFLECTIONS_LOG",
    "AI_MODE",
]