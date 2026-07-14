"""Generate an image from a text prompt with EcoHash (OpenAI-compatible)."""

import base64
import os

from openai import OpenAI

client = OpenAI(
    base_url="https://api.ecohash.com/v1",
    api_key=os.environ["ECOHASH_API_KEY"],
)

response = client.images.generate(
    model="z-image-turbo",
    prompt="a watercolor painting of a fox in a misty forest",
    size="1024x1024",            # also: 512x512, 768x768, 1024x768, 768x1024
    response_format="b64_json",  # or "url" (24-hour link)
    # seed=42,                   # deterministic output
)

with open("image.png", "wb") as f:
    f.write(base64.b64decode(response.data[0].b64_json))

print("wrote image.png")
