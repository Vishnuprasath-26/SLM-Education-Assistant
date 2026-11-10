
from pathlib import Path
import json

PROJECT_ROOT = Path(__file__).resolve().parents[2]

CONFIG_PATH = PROJECT_ROOT / "configs" / "optimized_config.json"


def load_config():

    with CONFIG_PATH.open("r", encoding="utf-8-sig") as file:
        config = json.load(file)

    return config


config = load_config()

MODEL_NAME = config["model_name"]
OLLAMA_API_URL = config["api_url"]
TEMPERATURE = config["temperature"]
MAX_NEW_TOKENS = config["max_new_tokens"]
TIMEOUT = config["timeout"]

PROMPT_INSTRUCTIONS = config["prompt_instructions"]
