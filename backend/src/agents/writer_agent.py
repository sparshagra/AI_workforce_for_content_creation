from src.llm.llama_api import call_llama

def run_writer(prompt: str, context: str = "") -> str:
    """Writer Agent — generates the first content draft."""
    full_prompt = f"{context}\n\n{prompt}" if context else prompt
    print("🧠  Writer Agent: Generating content...")
    return call_llama(full_prompt)
