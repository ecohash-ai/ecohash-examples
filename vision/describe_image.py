"""Describe an image with a vision model on EcoHash (OpenAI-compatible)."""

import os

from openai import OpenAI

client = OpenAI(
    base_url="https://api.ecohash.com/v1",
    api_key=os.environ["ECOHASH_API_KEY"],
)

image_url = "https://raw.githubusercontent.com/pytorch/hub/master/images/dog.jpg"

response = client.chat.completions.create(
    model="qwen3-vl-8b-instruct",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What is in this image?"},
                {"type": "image_url", "image_url": {"url": image_url}},
            ],
        }
    ],
)

print(response.choices[0].message.content)
