"""Function calling with EcoHash (OpenAI-compatible).

Full loop: the model requests a tool call, we run the tool, feed the result back,
and the model returns a final natural-language answer.
"""

import json
import os

from openai import OpenAI

client = OpenAI(
    base_url="https://api.ecohash.com/v1",
    api_key=os.environ["ECOHASH_API_KEY"],
)


def get_weather(city):
    # Stand-in for a real weather API.
    return {"city": city, "temp_c": 21, "condition": "sunny"}


tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get the current weather for a city.",
        "parameters": {
            "type": "object",
            "properties": {"city": {"type": "string"}},
            "required": ["city"],
        },
    },
}]

messages = [{"role": "user", "content": "What's the weather in Dallas? Answer in one sentence."}]

first = client.chat.completions.create(model="qwen2.5-7b-instruct", messages=messages, tools=tools)
msg = first.choices[0].message

if not msg.tool_calls:
    print(msg.content)
else:
    # Record the assistant's tool request, run each tool, append the results.
    messages.append({
        "role": "assistant",
        "content": msg.content,
        "tool_calls": [{
            "id": c.id, "type": "function",
            "function": {"name": c.function.name, "arguments": c.function.arguments},
        } for c in msg.tool_calls],
    })
    for c in msg.tool_calls:
        result = get_weather(**json.loads(c.function.arguments))
        messages.append({"role": "tool", "tool_call_id": c.id, "content": json.dumps(result)})

    final = client.chat.completions.create(model="qwen2.5-7b-instruct", messages=messages)
    print(final.choices[0].message.content)
