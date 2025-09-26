import time
from openai import OpenAI
from src.config import API_KEY, PROMPT_AI
from src.utils import encode_image

client = OpenAI(api_key=API_KEY)

def call_gpt(image_path, retries=3):
    """Send image to GPT with retries."""
    img_b64 = encode_image(image_path)

    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": PROMPT_AI},
                    {"role": "user", "content": [
                        {"type": "image_url", "image_url": {"url": img_b64}}
                    ]}
                ],
                max_tokens=300
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            wait_time = 2 ** attempt
            print(f"⚠️ Error on {image_path} (attempt {attempt+1}): {e}. Retrying in {wait_time}s...")
            time.sleep(wait_time)
    return f"ERROR: {e}"
