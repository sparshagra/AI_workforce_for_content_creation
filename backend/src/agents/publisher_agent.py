import os

def save_to_file(content: str, image_path: str, output_path="data/final_post.md"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    formatted = f"## Final Post\n\n{content}\n\n![Visual]({image_path})"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(formatted)
    return formatted

def run_publisher(content: str, image_path: str):
    """Publisher Agent — compiles content and image."""
    print("🗞️  Publisher Agent: Formatting final output...")
    return save_to_file(content, image_path)
