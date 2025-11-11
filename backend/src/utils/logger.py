from datetime import datetime
from src.config import LOG_PATH
import os

os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

def log_event(agent_name: str, message: str):
    """Simple timestamped logging for agent activity."""
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{agent_name}] {message}\n")
    print(f"🧩 {agent_name}: {message}")
