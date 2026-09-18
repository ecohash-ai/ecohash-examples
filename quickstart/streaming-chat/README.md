# Streaming chat

Stream a chat completion token by token over server-sent events, so output appears as
it is generated instead of all at once.

**How it works:** pass `stream=True` and iterate the chunks, printing each `delta`.

## Run

```bash
pip install openai
export ECOHASH_API_KEY=eco_...   # create one at https://console.ecohash.com?utm_source=github&utm_medium=referral&utm_campaign=devrel&utm_content=examples-streaming-chat
python stream.py
```

**Expected output:** a short haiku, printed word by word.

```
Here is a haiku about open source:

Code shared freely flows
Collaboration's sweet gift
Freedom's open door
```

The wording differs each run.

**Models:** `llama-3.1-8b-instruct` (default), `gpt-oss-20b`, `qwen3-coder-30b-a3b-instruct`, `GLM-5.2`.
**Docs:** [Chat completions](https://docs.ecohash.com/platform-models/chat-completions?utm_source=github&utm_medium=referral&utm_campaign=devrel&utm_content=examples-streaming-chat-docs).
