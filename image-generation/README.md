# Image generation

Generate an image from a text prompt and save it as a PNG.

**How it works:** call `images.generate` with `response_format="b64_json"`, then
base64-decode the result to bytes.

## Run

```bash
pip install openai
export ECOHASH_API_KEY=eco_...   # create one at console.ecohash.com
python generate.py
```

**Expected output:** an `image.png` (a watercolor fox in a misty forest).

**Models:** `z-image-turbo`.
**Docs:** [Image generation](https://docs.ecohash.com/platform-models/image-generation).
