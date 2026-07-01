"""Multi-turn chat with EcoHash (OpenAI-compatible). Type 'exit' to quit."""

import os

from openai import OpenAI

client = OpenAI(
    base_url="https://api.ecohash.com/v1",
    api_key=os.environ["ECOHASH_API_KEY"],
)

messages = [{"role": "system", "content": "You are a concise, helpful assistant."}]

print("Chat with EcoHash — type 'exit' to quit.")
while True:
    user = input("you> ").strip()
    if user.lower() in {"exit", "quit"}:
        break
    messages.append({"role": "user", "content": user})
    reply = client.chat.completions.create(
        model="llama-3.1-8b-instruct",
        messages=messages,
    ).choices[0].message.content
    print("bot>", reply)
    messages.append({"role": "assistant", "content": reply})
