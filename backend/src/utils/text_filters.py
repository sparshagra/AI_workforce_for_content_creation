BANNED_WORDS = ["hate", "violence", "discrimination", "illegal"]

def contains_banned_words(text: str) -> bool:
    """Check if text contains any banned or unsafe words."""
    text_lower = text.lower()
    return any(word in text_lower for word in BANNED_WORDS)
