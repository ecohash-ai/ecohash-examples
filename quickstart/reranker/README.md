# Reranker

Reorder candidate documents by relevance to a query — a common second stage in RAG,
after an initial embedding/keyword retrieval.

**How it works:** POST the query + documents to `/v1/rerank`; the response returns
document indices sorted by `relevance_score`.

## Run

```bash
pip install requests
export ECOHASH_API_KEY=eco_...   # create one at console.ecohash.com
python rerank.py
```

**Expected output:** the two most relevant documents (indices + scores) for the query
*"how does solar power work?"*.

**Models:** `bge-reranker-v2-m3`.
**Docs:** [Reranker](https://docs.ecohash.com/platform-models/reranker).
