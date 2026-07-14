"""Rerank documents by relevance with EcoHash."""

import os

import requests

response = requests.post(
    "https://api.ecohash.com/v1/rerank",
    headers={"Authorization": f"Bearer {os.environ['ECOHASH_API_KEY']}"},
    json={
        "model": "bge-reranker-v2-m3",
        "query": "how does solar power work?",
        "documents": [
            "Solar panels convert sunlight into electricity.",
            "My cat enjoys the sun but cannot generate power.",
            "Photovoltaic cells transform photons into electric current.",
        ],
        "top_n": 2,
    },
)

for item in response.json()["results"]:
    print(item["index"], item["relevance_score"])
