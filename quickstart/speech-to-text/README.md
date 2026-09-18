# Speech-to-text

Transcribe an audio file to text.

**How it works:** POST the audio to `/v1/audio/transcriptions` via the OpenAI SDK's
`audio.transcriptions.create`.

## Run

```bash
pip install openai
export ECOHASH_API_KEY=eco_...   # create one at https://console.ecohash.com?utm_source=github&utm_medium=referral&utm_campaign=devrel&utm_content=examples-speech-to-text
python transcribe.py path/to/audio.wav
```

No audio handy? On macOS you can make a test file in two commands:

```bash
say -o sample.aiff "EcoHash provides an OpenAI compatible API for open models."
afconvert -f WAVE -d LEI16@16000 -c 1 sample.aiff sample.wav
```

**Expected output:** the transcript, one line on stdout.

```
EcoHash provides an OpenAI-compatible API for open models.
```

**Models:** `whisper-large-v3-turbo` (default), `qwen3-asr-1-7b`, `fun-asr-nano`.
**Docs:** [Speech-to-text](https://docs.ecohash.com/platform-models/audio-transcription?utm_source=github&utm_medium=referral&utm_campaign=devrel&utm_content=examples-speech-to-text-docs).
