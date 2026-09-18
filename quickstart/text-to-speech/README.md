# Text-to-speech

Synthesize speech from text and save it to a file.

**How it works:** stream `/v1/audio/speech` to a `.wav` with the OpenAI SDK's
`audio.speech.with_streaming_response.create`.

## Run

```bash
pip install openai
export ECOHASH_API_KEY=eco_...   # create one at https://console.ecohash.com?utm_source=github&utm_medium=referral&utm_campaign=devrel&utm_content=examples-text-to-speech
python speak.py
```

**Expected output:** `wrote speech.wav` on stdout, and a `speech.wav` in the current
directory saying *"Hello from EcoHash."* (about 73 KB, 24 kHz mono).

**Models:** `kokoro-82m` (default, voice `af_heart`), `qwen3-tts`.
**Docs:** [Text-to-speech](https://docs.ecohash.com/platform-models/audio-speech?utm_source=github&utm_medium=referral&utm_campaign=devrel&utm_content=examples-text-to-speech-docs).
