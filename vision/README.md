# Vision

Ask a question about an image with a multimodal model.

**How it works:** send a chat message whose `content` mixes text and an `image_url`
(a public URL or a base64 `data:` URI).

## Run

```bash
pip install openai
export ECOHASH_API_KEY=eco_...   # create one at console.ecohash.com
python describe_image.py
```

**Expected output:** a description of the sample image (a dog).

**Models:** `qwen3-vl-8b-instruct`, `gemma-4-31b-it`.
**Docs:** [Chat completions](https://docs.ecohash.com/platform-models/chat-completions).
