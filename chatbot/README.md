# Chatbot — multi-turn

A minimal terminal chatbot that keeps conversation history, so the model remembers
earlier turns (not a one-shot request).

**How it works:** append each `user` and `assistant` turn to a `messages` list and
resend it every request.

## Run

```bash
pip install openai
export ECOHASH_API_KEY=eco_...   # create one at console.ecohash.com
python chat.py
```

**Expected output:** an interactive `you> / bot>` loop; type `exit` to quit.

**Models:** `llama-3.1-8b-instruct`, `qwen2.5-7b-instruct`, `GLM-5.2`, `Qwen3-235B-A22B`.
**Docs:** [Chat completions](https://docs.ecohash.com/platform-models/chat-completions).
