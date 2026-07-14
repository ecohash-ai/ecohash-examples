# Embeddings — semantic search

Turn text into vectors and rank documents by meaning — the core of semantic search
and RAG. This example embeds a few documents and a query in one call, then ranks the
documents by cosine similarity (no vector database needed for the demo).

**How it works:** embed `docs + [query]` in one request → cosine similarity → sort.

## Run

```bash
pip install openai
export ECOHASH_API_KEY=eco_...   # create one at console.ecohash.com
python embed.py
```

**Expected output:** the query *"How do I get an API key?"* ranks the *"Create an API key in the console"* document first.

**Models:** `jina-embeddings-v3`, `qwen3-embedding-8b` / `4b` / `0.6b`.
**Docs:** [Embeddings](https://docs.ecohash.com/platform-models/embeddings).
