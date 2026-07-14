# Streaming chat

Stream a chat completion token-by-token over server-sent events, so output appears as it is generated instead of all at once.

**How it works:** pass `stream=True` and iterate the chunks, printing each `delta`.

## Run

```bash
pip install openai
export ECOHASH_API_KEY=eco_...   # create one at console.ecohash.com
python stream.py
```

**Expected output:** a short haiku printed word-by-word.

**Models:** `llama-3.1-8b-instruct`, `qwen2.5-7b-instruct`, `GLM-5.2`.
**Docs:** [Chat completions](https://docs.ecohash.com/platform-models/chat-completions).
