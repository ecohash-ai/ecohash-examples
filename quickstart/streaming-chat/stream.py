"""Stream a chat completion from EcoHash (OpenAI-compatible)."""

import os
import sys

from openai import OpenAI

api_key = os.environ.get("ECOHASH_API_KEY")
if not api_key:
    sys.exit("ECOHASH_API_KEY is not set. Create a key at https://console.ecohash.com"
             "?utm_source=github&utm_medium=referral&utm_campaign=devrel"
             "&utm_content=examples-streaming-chat-missing-key, "

             "then: export ECOHASH_API_KEY=eco_...")

client = OpenAI(
    base_url="https://api.ecohash.com/v1",
    api_key=api_key,
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
