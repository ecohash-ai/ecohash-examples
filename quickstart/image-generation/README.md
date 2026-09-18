# Image generation

Generate an image from a text prompt and save it as a PNG.

**How it works:** call `images.generate` with `response_format="b64_json"`, then
base64-decode the result to bytes.

## Run

```bash
pip install openai
export ECOHASH_API_KEY=eco_...   # create one at https://console.ecohash.com?utm_source=github&utm_medium=referral&utm_campaign=devrel&utm_content=examples-image-generation
python generate.py
```

**Expected output:** `wrote image.png` on stdout, and a 1024x1024 `image.png` of a
watercolor fox in a misty forest (around 1.4 MB).

**Models:** `z-image-turbo` (default), `flux2-klein`, `qwen-image`.
**Docs:** [Image generation](https://docs.ecohash.com/platform-models/image-generation?utm_source=github&utm_medium=referral&utm_campaign=devrel&utm_content=examples-image-generation-docs).
