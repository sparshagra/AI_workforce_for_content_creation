"""
Writer Agent
------------
This agent is responsible for generating the initial text content (draft)
based on a given user prompt and optional context.

It uses the Llama 3.2 1B Instruct model hosted on Hugging Face
through the OpenAI-compatible API endpoint.
"""

import os
from openai import OpenAI

# ------------------------------
# Initialize Hugging Face Client
# ------------------------------
HF_TOKEN = os.environ.get("HF_TOKEN")

if not HF_TOKEN:
    raise ValueError("❌ Missing HF_TOKEN environment variable. Please set it before running.")

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=HF_TOKEN,
)

# ------------------------------
# Core Function
# ------------------------------
def run_writer(prompt: str, context: str = "") -> str:
    """
    Generate a text draft using the Llama-3.2-1B-Instruct model.

    Args:
        prompt (str): The main topic or user instruction.
        context (str): Optional background or previously generated info.

    Returns:
        str: Generated text content.
    """

    # Combine context (if any) with the user prompt
    full_prompt = f"{context}\n\n{prompt}" if context else prompt

    print("🧠  Writer Agent: Generating text using Llama 3.2 1B...")

    try:
        completion = client.chat.completions.create(
            model="meta-llama/Llama-3.2-1B-Instruct",
            messages=[{"role": "user", "content": full_prompt}],
            max_tokens=400,
            temperature=0.8,
        )

        draft = completion.choices[0].message.content.strip()

        print("✅  Writer Agent: Text generation completed.\n")
        return draft

    except Exception as e:
        print(f"❌  Writer Agent: Failed to generate text. Error: {e}")
        return "Error: Text generation failed."


# ------------------------------
# Optional Standalone Test
# ------------------------------
if __name__ == "__main__":
    test_prompt = "Write a short Diwali-themed marketing post for a dairy brand."
    result = run_writer(test_prompt)
    print("\n📝 Generated Draft:\n", result)
