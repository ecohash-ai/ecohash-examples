# jina-embeddings-v3 via the EcoHash API

`jina-embeddings-v3` is an open text-embedding model for semantic search, RAG, and clustering. Call it through EcoHash's OpenAI-compatible API — one key.

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.ecohash.com/v1", api_key="eco_...")

resp = client.embeddings.create(
    model="jina-embeddings-v3",
    input=["EcoHash is an OpenAI-compatible inference API."],
)
print(len(resp.data[0].embedding))
```

- Get a key: [console.ecohash.com](https://console.ecohash.com?utm_source=github)
- Docs: [Embeddings](https://docs.ecohash.com/platform-models/embeddings)
- Runnable example: [../embeddings](../embeddings)
- Other embedding models: `qwen3-embedding-8b`, `qwen3-embedding-4b`, `qwen3-embedding-0.6b`
