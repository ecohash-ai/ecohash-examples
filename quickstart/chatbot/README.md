# Chatbot: multi-turn

A terminal chatbot that keeps conversation history, so the model remembers earlier
turns instead of answering each message cold.

**How it works:** append each `user` and `assistant` turn to a `messages` list and
resend the list every request.

## Run

```bash
pip install openai
export ECOHASH_API_KEY=eco_...   # create one at https://console.ecohash.com?utm_source=github&utm_medium=referral&utm_campaign=devrel&utm_content=examples-chatbot
python chat.py
```

**Expected output:** a `you> / bot>` loop. Type `exit` to quit.

```
Chat with EcoHash. Type 'exit' to quit.
you> My name is Wei.
bot> Nice to meet you, Wei! Is there something I can help you with today?
you> What is my name?
bot> Your name is Wei.
```

The second answer is the point: the model only knows your name because the first turn
is still in `messages`.

**Models:** `llama-3.1-8b-instruct` (default), `gpt-oss-20b`, `qwen3-coder-30b-a3b-instruct`, `GLM-5.2`.
**Docs:** [Chat completions](https://docs.ecohash.com/platform-models/chat-completions?utm_source=github&utm_medium=referral&utm_campaign=devrel&utm_content=examples-chatbot-docs).
