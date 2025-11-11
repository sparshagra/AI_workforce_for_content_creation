import os
from huggingface_hub import InferenceClient

HF_TOKEN = os.environ["HF_TOKEN"]

# ---------- TEXT (Llama-3.2-1B-Instruct) ----------
from openai import OpenAI

client_text = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=HF_TOKEN,
)

text_prompt = (
    "We are Ufresh, a dairy brand. Create a Diwali-themed social-media ad script."
)

completion = client_text.chat.completions.create(
    model="meta-llama/Llama-3.2-1B-Instruct",
    messages=[{"role": "user", "content": text_prompt}],
    max_tokens=300,
)
script_text = completion.choices[0].message.content
print("\n🧠  Generated Script:\n", script_text)

# ---------- IMAGE (Stable-Diffusion XL via HF InferenceClient) ----------
client_image = InferenceClient(
    provider="nscale",
    api_key=HF_TOKEN,
)

image_prompt = (
    "I will be providing you with the script of the ad campaign. The topic of the campaign will be, "
)

print("\n🎨  Generating image via Hugging Face Inference API…")

image = client_image.text_to_image(
    image_prompt + script_text,
    model="stabilityai/stable-diffusion-xl-base-1.0",
)

output_path = "ufresh_diwali_ad.png"
image.save(output_path)

print(f"✅  Saved image to {output_path}")


# from huggingface_hub import InferenceClient
# import os

# # Initialize the client
# client = InferenceClient(
#     provider="nscale",
#     api_key=os.environ["HF_TOKEN"],
# )

# # Generate the image
# image = client.text_to_image(
#     "Astronaut riding a horse",
#     model="stabilityai/stable-diffusion-xl-base-1.0",
# )

# # Save the image
# image.save("output.png")

# print("✅ Image saved as output.png")
## check