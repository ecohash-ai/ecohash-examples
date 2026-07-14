<p align="center">
  <a href="https://ecohash.com"><img src="assets/ecohash-logo.png" alt="EcoHash" width="280"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-blue" alt="MIT">
  <a href="https://docs.ecohash.com"><img src="https://img.shields.io/badge/documentation-6D28D9" alt="Documentation"></a>
  <a href="https://x.com/ecohashdev"><img src="https://img.shields.io/badge/X-@ecohashdev-000000?logo=x&logoColor=white" alt="X"></a>
  <a href="https://huggingface.co/ecohash-ai"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-ecohash--ai-FFD21E" alt="Hugging Face"></a>
</p>

# EcoHash Examples

A collection of runnable example apps built on EcoHash — an OpenAI-compatible inference API for open models (chat, speech, embeddings, images).

## New to EcoHash?

Create an API key at [console.ecohash.com](https://console.ecohash.com?utm_source=github) and read the [docs](https://docs.ecohash.com). Every example points the OpenAI SDK at EcoHash:

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.ecohash.com/v1", api_key="eco_...")
```

Coming from another provider? See [how EcoHash compares](#comparison) below.

## Prerequisites

- An EcoHash API key, set as the `ECOHASH_API_KEY` environment variable.
- Python 3.9+. Each folder's README lists its `pip install` line.

## Voice & speech

- **[voice-agent](voice-agent)** — speech-to-text → LLM → text-to-speech, all on one API key
- **[speech-to-text](quickstart/speech-to-text)** — transcribe audio to text
- **[text-to-speech](quickstart/text-to-speech)** — synthesize speech from text

## Text

- **[chatbot](quickstart/chatbot)** — a minimal chat completion
- **[streaming-chat](quickstart/streaming-chat)** — stream the response as it generates
- **[function-calling](quickstart/function-calling)** — let the model call your tools

## Retrieval

- **[embeddings](quickstart/embeddings)** — turn text into vectors
- **[reranker](quickstart/reranker)** — reorder candidates by relevance

## Images

- **[image-generation](quickstart/image-generation)** — generate images from a text prompt

## Integrations

- **[vapi](integrations/vapi)** — Kokoro TTS as the voice of a Vapi voice agent (custom-voice adapter)

More platform integrations live in [integrations](integrations).

## Comparison

All three expose an OpenAI-compatible API — moving between them is mostly a `base_url` + key change. Facts from each project's own docs/site (2026-06); corrections welcome via issue.

| | EcoHash | OpenRouter | Together AI |
|---|---|---|---|
| What it is | Hosts open models + GPU cloud | Router to 300+ models across providers | Hosts open models + GPU cloud |
| Hosts the models | Yes | No (routes to providers) | Yes |
| One key covers | Chat, speech-to-text, text-to-speech, embeddings, reranker, images | Primarily chat/LLMs (others vary) | Chat, vision, embeddings, images, audio/video |
| Speech (STT + TTS) | STT **and** TTS | Varies by provider | STT (fast); TTS varies |
| Fine-tuning | Yes | No (it is a router) | Yes |
| Rent GPUs / clusters | Yes | No | Yes |
| Pricing | Per-token / per-minute | Pass-through + 5.5% fee on credits | Per-token + GPU hourly |

Sources: [EcoHash](https://docs.ecohash.com) · [OpenRouter](https://openrouter.ai) · [Together AI](https://www.together.ai).

## Getting help

- Documentation: https://docs.ecohash.com
- Questions or bugs: open an issue in this repo.

## License

MIT — see [LICENSE](LICENSE).
