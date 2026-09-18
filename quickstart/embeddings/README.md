# Embeddings: semantic search

Turn text into vectors and rank documents by meaning, the core of semantic search and
RAG. This example embeds a few documents and a query in one call, then ranks the
documents by cosine similarity. No vector database needed for the demo.

**How it works:** embed `docs + [query]` in one request, compute cosine similarity, sort.

## Run

```bash
pip install openai
export ECOHASH_API_KEY=eco_...   # create one at https://console.ecohash.com?utm_source=github&utm_medium=referral&utm_campaign=devrel&utm_content=examples-embeddings
python embed.py
```

**Expected output:** the query *"How do I get an API key?"* puts the console document first.

```
Query: How do I get an API key?

0.691  Create an API key in the console at console.ecohash.com.
0.336  EcoHash is an OpenAI-compatible inference API for open models.
0.128  Kokoro is a small, fast text-to-speech model.
0.082  Whisper transcribes speech to text in many languages.
```

Scores shift slightly between runs; the ordering is what matters.

**Models:** `jina-embeddings-v3` (default), `jina-embeddings-v4`, `qwen3-embedding-0.6b`.
**Docs:** [Embeddings](https://docs.ecohash.com/platform-models/embeddings?utm_source=github&utm_medium=referral&utm_campaign=devrel&utm_content=examples-embeddings-docs).
