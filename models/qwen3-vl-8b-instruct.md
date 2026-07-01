# qwen3-vl-8b-instruct via the EcoHash API

`qwen3-vl-8b-instruct` is an open vision-language model — ask questions about images. Call it through EcoHash's OpenAI-compatible API — one key.

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.ecohash.com/v1", api_key="eco_...")

resp = client.chat.completions.create(
    model="qwen3-vl-8b-instruct",
    messages=[{"role": "user", "content": [
        {"type": "text", "text": "What is in this image?"},
        {"type": "image_url", "image_url": {"url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/640px-Cat03.jpg"}},
    ]}],
)
print(resp.choices[0].message.content)
```

- Get a key: [console.ecohash.com](https://console.ecohash.com?utm_source=github)
- Docs: [Chat completions](https://docs.ecohash.com/platform-models/chat-completions)
- Runnable example: [../vision](../vision)
- Other vision models: `gemma-4-31b-it`
