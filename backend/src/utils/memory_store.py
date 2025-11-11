import json, os

MEMORY_PATH = "data/memory.json"

def save_memory(agent: str, data):
    """Save each agent’s output to memory file."""
    os.makedirs(os.path.dirname(MEMORY_PATH), exist_ok=True)
    try:
        if os.path.exists(MEMORY_PATH):
            with open(MEMORY_PATH, "r", encoding="utf-8") as f:
                memory = json.load(f)
        else:
            memory = {}
        memory[agent] = data
        with open(MEMORY_PATH, "w", encoding="utf-8") as f:
            json.dump(memory, f, indent=4)
    except Exception as e:
        print(f"❌ Memory error: {e}")

def read_memory(agent: str):
    if os.path.exists(MEMORY_PATH):
        with open(MEMORY_PATH, "r", encoding="utf-8") as f:
            memory = json.load(f)
        return memory.get(agent)
    return None
