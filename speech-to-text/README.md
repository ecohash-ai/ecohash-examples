# Speech-to-text

Transcribe an audio file to text.

**How it works:** POST the audio to `/v1/audio/transcriptions` via the OpenAI SDK's
`audio.transcriptions.create`.

## Run

```bash
pip install openai
export ECOHASH_API_KEY=eco_...   # create one at console.ecohash.com
python transcribe.py path/to/audio.wav
```

**Expected output:** the transcript text of the audio.

**Models:** `whisper-large-v3`, `qwen3-asr-1-7b`, `fun-asr-nano`.
**Docs:** [Speech-to-text](https://docs.ecohash.com/platform-models/audio-transcription).
