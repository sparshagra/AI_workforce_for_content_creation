from huggingface_hub import InferenceClient
from src.config import HF_TOKEN, IMAGE_MODEL
import os

client = InferenceClient(provider="nscale", api_key=HF_TOKEN)

def generate_visual(prompt: str, output_path="data/generated_image.png"):
    """Generate an image from text using Stable Diffusion XL."""
    print("🎨  Designer Agent: Generating image...")
    image = client.text_to_image(prompt, model=IMAGE_MODEL)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    image.save(output_path)
    print(f"✅  Image saved at {output_path}")
    return output_path
