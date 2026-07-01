# GLM-5.2 via the EcoHash API

`GLM-5.2` is an open large language model. Call it through EcoHash's OpenAI-compatible API — one key, drop-in with the OpenAI SDK.

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.ecohash.com/v1", api_key="eco_...")

resp = client.chat.completions.create(
    model="GLM-5.2",
    messages=[{"role": "user", "content": "Explain retrieval-augmented generation in two sentences."}],
)
print(resp.choices[0].message.content)
```

- Get a key: [console.ecohash.com](https://console.ecohash.com?utm_source=github)
- Docs: [Chat completions](https://docs.ecohash.com/platform-models/chat-completions)
- Runnable examples: [../chatbot](../chatbot), [../streaming-chat](../streaming-chat)
- Other LLMs: `llama-3.1-8b-instruct`, `qwen2.5-7b-instruct`, `Qwen3-235B-A22B`, `DeepSeek-V4-Flash`
