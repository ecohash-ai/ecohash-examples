# Reranker

Reorder candidate documents by relevance to a query, a common second stage in RAG
after an initial embedding or keyword retrieval.

**How it works:** POST the query and documents to `/v1/rerank`; the response returns
document indices sorted by `relevance_score`.

## Run

```bash
pip install requests
export ECOHASH_API_KEY=eco_...   # create one at https://console.ecohash.com?utm_source=github&utm_medium=referral&utm_campaign=devrel&utm_content=examples-reranker
python rerank.py
```

**Expected output:** the top two documents for *"how does solar power work?"*, as
`index score` pairs.

```
0 0.3991473317146301
2 0.016313889995217323
```

Index 1, the one about a cat enjoying the sun, is correctly left out by `top_n: 2`.

**Models:** `bge-reranker-v2-m3`.
**Docs:** [Reranker](https://docs.ecohash.com/platform-models/reranker?utm_source=github&utm_medium=referral&utm_campaign=devrel&utm_content=examples-reranker-docs).
