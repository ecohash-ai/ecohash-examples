# Integrations

Adapters and configurations for plugging EcoHash into agent platforms, coding tools,
gateways and automation apps. Every integration uses the same OpenAI-compatible API at
`https://api.ecohash.com/v1` and one API key.

| Integration | What it does | Where it lives |
| --- | --- | --- |
| [vapi](vapi) | Kokoro TTS as the voice of a Vapi agent (custom-voice adapter) | this repo |
| [retell](retell) | an open model as the brain of a Retell AI agent (custom LLM bridge) | this repo |
| Dify | model provider plugin, published on the Dify Marketplace | [ecohash-dify-plugin](https://github.com/ecohash-ai/ecohash-dify-plugin) |

Planned: LiteLLM, Open WebUI, coding agents (Cursor, Cline, Aider), n8n, MacWhisper,
and Bazarr/Subgen.
