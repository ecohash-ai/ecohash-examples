# whisper-large-v3 via the EcoHash API

`whisper-large-v3` is an open speech-to-text model covering 99 languages. Call it through EcoHash's OpenAI-compatible API — one key, no per-model account.

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.ecohash.com/v1", api_key="eco_...")

with open("audio.wav", "rb") as audio_file:
    result = client.audio.transcriptions.create(model="whisper-large-v3", file=audio_file)

print(result.text)
```

- Get a key: [console.ecohash.com](https://console.ecohash.com?utm_source=github)
- Docs: [Speech-to-text](https://docs.ecohash.com/platform-models/audio-transcription)
- Runnable example: [../speech-to-text](../speech-to-text)
- Other STT models: `qwen3-asr-1-7b`, `fun-asr-nano`
