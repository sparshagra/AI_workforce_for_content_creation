import os

# Get Hugging Face token from environment
HF_TOKEN = os.environ.get("HF_TOKEN")

if not HF_TOKEN:
    raise ValueError("❌ Missing HF_TOKEN. Please set it in your environment variables.")

# Model names
LLAMA_MODEL = "meta-llama/Llama-3.2-1B-Instruct"
IMAGE_MODEL = "stabilityai/stable-diffusion-xl-base-1.0"

# Output paths
OUTPUT_DIR = "data/"
LOG_PATH = os.path.join(OUTPUT_DIR, "logs", "agent_logs.txt")
