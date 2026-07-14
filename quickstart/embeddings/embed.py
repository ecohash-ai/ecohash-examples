"""Semantic search with EcoHash embeddings (OpenAI-compatible).

Embed a few documents and a query, then rank the documents by cosine similarity.
"""

import os

from openai import OpenAI

client = OpenAI(
    base_url="https://api.ecohash.com/v1",
    api_key=os.environ["ECOHASH_API_KEY"],
)

docs = [
    "EcoHash is an OpenAI-compatible inference API for open models.",
    "Create an API key in the console at console.ecohash.com.",
    "Kokoro is a small, fast text-to-speech model.",
    "Whisper transcribes speech to text in many languages.",
]
query = "How do I get an API key?"

# One call embeds every document plus the query.
data = client.embeddings.create(model="jina-embeddings-v3", input=docs + [query]).data
doc_vecs = [d.embedding for d in data[:-1]]
q_vec = data[-1].embedding


def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    norm = (sum(x * x for x in a) ** 0.5) * (sum(y * y for y in b) ** 0.5)
    return dot / norm


ranked = sorted(zip((cosine(q_vec, v) for v in doc_vecs), docs), reverse=True)
print(f"Query: {query}\n")
for score, doc in ranked:
    print(f"{score:.3f}  {doc}")
