# kokoro-82m via the EcoHash API

`kokoro-82m` is a small, fast open text-to-speech model. Call it through EcoHash's OpenAI-compatible API — one key, no per-model account.

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.ecohash.com/v1", api_key="eco_...")

with client.audio.speech.with_streaming_response.create(
    model="kokoro-82m",
    voice="af_heart",
    input="Hello from EcoHash.",
    response_format="wav",
) as response:
    response.stream_to_file("speech.wav")
```

- Get a key: [console.ecohash.com](https://console.ecohash.com?utm_source=github)
- Docs: [Text-to-speech](https://docs.ecohash.com/platform-models/audio-speech)
- Runnable example: [../text-to-speech](../text-to-speech)
- Other TTS models: `qwen3-tts`
