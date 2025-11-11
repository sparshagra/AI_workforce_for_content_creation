from src.llm.image_gen_api import generate_visual
import re

def extract_keywords(text: str, n: int = 5):
    """Simple keyword extractor."""
    words = re.findall(r'\b[A-Za-z]{4,}\b', text)
    keywords = list(dict.fromkeys(words))[:n]
    return ", ".join(keywords)

def run_designer(content: str) -> str:
    """Designer Agent — generates an image prompt from content."""
    keywords = extract_keywords(content)
    image_prompt = f"Visualize a concept related to: {keywords}"
    return generate_visual(image_prompt)
