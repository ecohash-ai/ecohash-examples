# qwen3-coder-30b-a3b-instruct via the EcoHash API

`qwen3-coder-30b-a3b-instruct` is an open code-focused large language model. Call it through EcoHash's OpenAI-compatible API — one key, drop-in with the OpenAI SDK.

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.ecohash.com/v1", api_key="eco_...")

resp = client.chat.completions.create(
    model="qwen3-coder-30b-a3b-instruct",
    messages=[{"role": "user", "content": "Write a Python function that reverses a linked list."}],
)
print(resp.choices[0].message.content)
```

- Get a key: [console.ecohash.com](https://console.ecohash.com?utm_source=github)
- Docs: [Chat completions](https://docs.ecohash.com/platform-models/chat-completions)
- Runnable examples: [../chatbot](../chatbot), [../function-calling](../function-calling)
