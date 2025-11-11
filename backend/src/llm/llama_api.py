from openai import OpenAI
from src.config import HF_TOKEN, LLAMA_MODEL

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=HF_TOKEN,
)

def call_llama(prompt: str, max_tokens: int = 400, temperature: float = 0.8) -> str:
    """Generate text from Hugging Face Llama 3.2."""
    completion = client.chat.completions.create(
        model=LLAMA_MODEL,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens,
        temperature=temperature,
    )
    return completion.choices[0].message.content.strip()
