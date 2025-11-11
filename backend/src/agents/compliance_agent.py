from src.utils.text_filters import contains_banned_words

def run_compliance(content: str) -> dict:
    """Compliance Agent — ensures ethical and copyright-safe text."""
    if contains_banned_words(content):
        return {"approved": False, "reason": "Contains restricted or unsafe terms."}
    return {"approved": True}
