import json
from pathlib import Path

DEFAULT_CONFIG = {
    "data_file": "data/students.json",
    "log_file": "logs/app.log",
    "json_indent": 2
}

def load_config(path: str = "config/config.json") -> dict:
    p = Path(path)
    if not p.exists():
        return DEFAULT_CONFIG
    try:
        with open(p, "r", encoding="utf-8") as f:
            cfg = json.load(f)
            merged = {**DEFAULT_CONFIG, **cfg}
            return merged
    except Exception:
        return DEFAULT_CONFIG