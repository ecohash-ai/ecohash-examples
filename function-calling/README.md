# Function / tool calling

The full tool-use loop: the model requests a tool call, your code runs the tool, you
feed the result back, and the model returns a final natural-language answer.

**How it works:** send `tools` → model returns a `tool_call` → run the function →
append a `tool` message with the result → model produces the final answer.

## Run

```bash
pip install openai
export ECOHASH_API_KEY=eco_...   # create one at console.ecohash.com
python tools.py
```

**Expected output:** a one-sentence weather answer for Dallas, composed from the tool result (`21°C, sunny`).

**Models:** `qwen2.5-7b-instruct`, `GLM-5.2` (models with tool calling enabled).
**Docs:** [Chat completions](https://docs.ecohash.com/platform-models/chat-completions).
