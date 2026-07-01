"""Stream a chat completion from EcoHash (OpenAI-compatible)."""

import os

from openai import OpenAI

client = OpenAI(
    base_url="https://api.ecohash.com/v1",
    api_key=os.environ["ECOHASH_API_KEY"],
)

stream = client.chat.completions.create(
    model="llama-3.1-8b-instruct",
    messages=[{"role": "user", "content": "Write a haiku about open source."}],
    stream=True,
    # temperature=0.7,   # 0–2
    # max_tokens=256,
)

for chunk in stream:
    if not chunk.choices:          # final usage chunk carries no choices
        continue
    delta = chunk.choices[0].delta.content
    if delta:
        print(delta, end="", flush=True)
print()
