"""Multi-turn chat with EcoHash (OpenAI-compatible). Type 'exit' to quit."""

import os
import sys

from openai import OpenAI

api_key = os.environ.get("ECOHASH_API_KEY")
if not api_key:
    sys.exit("ECOHASH_API_KEY is not set. Create a key at https://console.ecohash.com"
             "?utm_source=github&utm_medium=referral&utm_campaign=devrel"
             "&utm_content=examples-chatbot-missing-key, "

             "then: export ECOHASH_API_KEY=eco_...")

client = OpenAI(
    base_url="https://api.ecohash.com/v1",
    api_key=api_key,
)

messages = [{"role": "system", "content": "You are a concise, helpful assistant."}]

print("Chat with EcoHash. Type 'exit' to quit.")
while True:
    user = input("you> ").strip()
    if user.lower() in {"exit", "quit"}:
        break
    messages.append({"role": "user", "content": user})
    reply = client.chat.completions.create(
        model="llama-3.1-8b-instruct",
        messages=messages,
        # temperature=0.7,   # 0–2
        # max_tokens=512,
    ).choices[0].message.content
    print("bot>", reply)
    messages.append({"role": "assistant", "content": reply})
