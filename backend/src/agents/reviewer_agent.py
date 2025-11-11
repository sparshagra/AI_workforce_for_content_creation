def run_reviewer(draft: str) -> dict:
    """Reviewer Agent — checks tone and clarity."""
    # Basic heuristics or lightweight model could be used
    feedback = []
    if len(draft.split()) < 30:
        feedback.append("Too short — add more context.")
    if "!" in draft:
        feedback.append("Tone: slightly informal due to exclamation marks.")

    approved = len(feedback) == 0
    return {
        "approved": approved,
        "feedback": feedback if feedback else ["Looks good!"]
    }
