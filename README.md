<p align="center">
  <img src="assets/ecohash-logo.png" alt="EcoHash" width="280">
</p>

<p align="center">
  <a href="https://console.ecohash.com?utm_source=github">Platform</a> •
  <a href="https://docs.ecohash.com">Docs</a> •
  <a href="https://ecohash.com">Website</a>
</p>

# EcoHash Examples

A collection of runnable example apps built on EcoHash — an OpenAI-compatible inference API for open models (chat, vision, speech, embeddings, images).

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-blue" alt="MIT">
  <img src="https://img.shields.io/badge/OpenAI-compatible-6D28D9" alt="OpenAI-compatible">
  <img src="https://img.shields.io/badge/examples-10-lightgrey" alt="10 examples">
</p>

## New to EcoHash?

Create an API key at [console.ecohash.com](https://console.ecohash.com?utm_source=github) and read the [docs](https://docs.ecohash.com). Every example points the OpenAI SDK at EcoHash:

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.ecohash.com/v1", api_key="eco_...")
```

Coming from another provider? See [how EcoHash compares to OpenRouter and Together](comparison.md). Want a specific model? Jump to [model quickstarts](models).

## Prerequisites

- An EcoHash API key, set as the `ECOHASH_API_KEY` environment variable.
- Python 3.9+. Each folder's README lists its `pip install` line.

## Voice & speech

- **[voice-agent](voice-agent)** — speech-to-text → LLM → text-to-speech, all on one API key
- **[speech-to-text](speech-to-text)** — transcribe audio to text
- **[text-to-speech](text-to-speech)** — synthesize speech from text

## Text

- **[chatbot](chatbot)** — a minimal chat completion
- **[streaming-chat](streaming-chat)** — stream the response as it generates
- **[function-calling](function-calling)** — let the model call your tools

## Retrieval

- **[embeddings](embeddings)** — turn text into vectors
- **[reranker](reranker)** — reorder candidates by relevance

## Vision & images

- **[vision](vision)** — ask questions about an image
- **[image-generation](image-generation)** — generate images from a text prompt

## Getting help

- Documentation: https://docs.ecohash.com
- Questions or bugs: open an issue in this repo.

## License

MIT — see [LICENSE](LICENSE).
