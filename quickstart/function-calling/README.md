# Function and tool calling

The full tool-use loop: the model requests a tool call, your code runs the tool, you
feed the result back, and the model returns a final natural-language answer.

**How it works:** send `tools`, the model returns a `tool_call`, you run the function,
append a `tool` message with the result, and the model composes the final answer.

## Run

```bash
pip install openai
export ECOHASH_API_KEY=eco_...   # create one at https://console.ecohash.com?utm_source=github&utm_medium=referral&utm_campaign=devrel&utm_content=examples-function-calling
python tools.py
```

**Expected output:** one sentence, composed from the stub tool's result (`21°C, sunny`).

```
The weather in Dallas is sunny with a temperature of 21°C.
```

**Models:** this needs a model with tool calling enabled. The catalog marks those with
`agent_capable: true`, so you can list them without guessing:

```bash
curl -s https://api.ecohash.com/platform/models \
  | python3 -c "import json,sys; [print(m['model_id']) for m in json.load(sys.stdin) if m.get('agent_capable')]"
```

`qwen3-coder-30b-a3b-instruct` is the default here. `GLM-5.2` and `qwen3.5-35b-a3b` also work.
**Docs:** [Chat completions](https://docs.ecohash.com/platform-models/chat-completions?utm_source=github&utm_medium=referral&utm_campaign=devrel&utm_content=examples-function-calling-docs).
