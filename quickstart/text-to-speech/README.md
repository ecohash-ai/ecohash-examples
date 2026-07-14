# Text-to-speech

Synthesize speech from text and save it to a file.

**How it works:** stream `/v1/audio/speech` to a `.wav` with the OpenAI SDK's
`audio.speech.with_streaming_response.create`.

## Run

```bash
pip install openai
export ECOHASH_API_KEY=eco_...   # create one at console.ecohash.com
python speak.py
```

**Expected output:** a `speech.wav` file saying *"Hello from EcoHash."*

**Models:** `kokoro-82m` (voice `af_heart`), `qwen3-tts`.
**Docs:** [Text-to-speech](https://docs.ecohash.com/platform-models/audio-speech).
