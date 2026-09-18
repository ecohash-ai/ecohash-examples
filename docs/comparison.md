# How EcoHash compares

Facts checked 2026-09-18 against each project's own site, API and docs. Prices and
counts move often, so treat this as a snapshot and verify anything you are about to
build a budget on. Corrections are welcome: open an issue.

All three speak the OpenAI API, so moving between them is a `base_url` and key change.

| | EcoHash | OpenRouter | Together AI |
|---|---|---|---|
| What it is | Hosts open models, rents GPUs | Router across providers | Hosts open models, rents GPUs |
| Runs the models | Yes | No, routes to providers | Yes |
| Models listed | 39 | 445 | serverless catalog across 9 categories |
| One key covers | chat, vision, STT, TTS, voice cloning, speaker diarization, embeddings, rerank, images, video, music | chat, vision, and some image and audio output, varying by provider | chat, vision, images, audio, video, transcription, embeddings, rerank, moderation |
| Speech in and out | both | depends on the provider routed to | both |
| Fine-tuning | yes | no, it is a router | yes |
| Rent GPUs or clusters | yes | no | yes |
| How you pay | per token or per minute, no platform fee | provider list price passed through, plus 5.5% on credit purchases ($0.80 minimum, 5% for crypto) | per token, plus hourly for GPUs |

Sources: [EcoHash catalog](https://api.ecohash.com/platform/models) and
[docs](https://docs.ecohash.com?utm_source=github&utm_medium=referral&utm_campaign=devrel&utm_content=examples-comparison-docs) ·
[OpenRouter FAQ](https://openrouter.ai/docs/faq) and [models API](https://openrouter.ai/api/v1/models) ·
[Together AI pricing](https://www.together.ai/pricing).

## What the table does not tell you

The category counts say nothing about which specific model you need or what it costs
on each platform. Kokoro TTS, for example, is served by both EcoHash and Together AI,
but they meter it differently: EcoHash bills per minute of audio, Together AI per
million characters. Compare the models you actually plan to call.

A router and a host solve different problems. OpenRouter is the better fit when you
want one key that reaches proprietary models from several vendors and automatic
failover between them. EcoHash and Together AI are hosts: fewer models, but you are
talking to the machines that serve them, which is what makes per-model pricing and
dedicated capacity possible.

Of the 39 models in the EcoHash catalog, 28 run on our own hardware and 11 are served
through an upstream provider. Both are reachable on the same key and the same base URL.

## Current EcoHash prices

Read them from the public catalog rather than trusting a table in a repo:

```bash
curl -s https://api.ecohash.com/platform/models | python3 -m json.tool | head -40
```

Each entry carries `model_id`, `category`, `context_length`,
`input_price_per_1m_tokens`, `output_price_per_1m_tokens` and `status`. The same
endpoint is what [check_setup.py](../check_setup.py) uses to catch models that have
been retired out from under these examples.

Or browse them with prices at
[ecohash.com/models](https://ecohash.com/models?utm_source=github&utm_medium=referral&utm_campaign=devrel&utm_content=examples-comparison-models).
