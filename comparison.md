# EcoHash vs OpenRouter vs Together AI

All three expose an **OpenAI-compatible API**, so moving between them is mostly a `base_url` + key change. They differ in *what they are* (a model host vs a router), which modalities you get from **one key**, and whether they also offer GPU compute and fine-tuning.

Facts below are from each project's own docs/site (linked at the bottom), as of 2026-06. Out of date or wrong? Please open an issue.

| | EcoHash | OpenRouter | Together AI |
|---|---|---|---|
| What it is | Inference provider hosting open models, plus GPU cloud | Router / aggregator to 300+ models across many providers | AI cloud hosting open models, plus GPU cloud |
| OpenAI-compatible | Yes | Yes | Yes |
| Hosts the models | Yes (own infrastructure) | No — routes to other providers | Yes (own infrastructure) |
| Models | Curated open models | 300+ open **and** closed, many providers | Open models |
| One key covers | Chat, vision, speech-to-text, text-to-speech, embeddings, reranker, images | Primarily chat / LLMs (image, audio, embeddings vary by provider) | Chat, vision, code, embeddings, images, audio/video |
| Speech (STT + TTS) | STT **and** TTS | Varies by underlying provider | STT (fast); TTS varies |
| Fine-tuning | Yes | No (it is a router) | Yes (LoRA, DPO, tool-call, 100B+) |
| Rent GPUs / clusters | Yes | No | Yes (on-demand, incl. B200) |
| Deploy your own model | Yes | No | Yes |
| Pricing model | Per-token / per-minute (own pricing) | Pass-through provider price + 5.5% fee on credits | Own per-token + GPU hourly |

**In short:** OpenRouter fits when you want one key to reach *many vendors' models* (including closed ones) and don't mind it being text-first. Together AI and EcoHash both *host* open models with OpenAI-compatible APIs, fine-tuning, and GPU compute; EcoHash's single key additionally covers speech-to-text **and** text-to-speech alongside chat, vision, embeddings, and images.

What EcoHash serves and how to call it: **[docs.ecohash.com](https://docs.ecohash.com)** · runnable [examples](README.md).

## Sources

- EcoHash — https://docs.ecohash.com
- OpenRouter — https://openrouter.ai · https://openrouter.ai/models
- Together AI — https://www.together.ai · https://docs.together.ai
