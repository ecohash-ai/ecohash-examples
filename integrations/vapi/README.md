# Vapi + EcoHash: custom TTS with Kokoro

Vapi lets you swap the voice of an agent for any TTS through its custom-voice provider: it POSTs the text to your server and plays back whatever PCM you return. This adapter puts Kokoro on EcoHash behind that slot, about $0.006 per minute of generated speech.

```
Vapi assistant ──voice-request──▶ server.py ──/v1/audio/speech──▶ EcoHash (kokoro-82m)
               ◀──raw PCM 16-bit mono──┘
```

1. Vapi POSTs `{"message": {"type": "voice-request", "text": ..., "sampleRate": ...}}` to your server.
2. The adapter calls EcoHash `/v1/audio/speech` with `model: kokoro-82m` and `response_format: pcm`.
3. Kokoro returns 24 kHz PCM; the adapter resamples if Vapi asked for a different rate.
4. The adapter answers with `application/octet-stream` PCM, and the caller hears Kokoro.

## Run

```bash
pip install fastapi uvicorn httpx numpy
export ECOHASH_API_KEY=eco_...          # create one at console.ecohash.com
export VAPI_SECRET=your-webhook-secret
uvicorn server:app --host 0.0.0.0 --port 8000
```

Expose the port publicly (ngrok is fine for a first test).

## Point the assistant at it

```json
{
  "voice": {
    "provider": "custom-voice",
    "server": {
      "url": "https://your-host.example.com/synthesize",
      "secret": "your-webhook-secret",
      "timeoutSeconds": 30
    }
  }
}
```

Vapi sends the secret back in the `x-vapi-secret` header on every request, and the adapter rejects anything that does not match.

## Test it without making a call

```bash
curl -s http://localhost:8000/synthesize \
  -H "Content-Type: application/json" \
  -H "x-vapi-secret: your-webhook-secret" \
  -d '{"message":{"type":"voice-request","text":"Your order number seven two nine is confirmed.","sampleRate":16000}}' \
  -o reply.pcm

ffplay -f s16le -ar 16000 -ch_layout mono reply.pcm
```

We ran this loop at 8, 16, and 24 kHz and fed the resampled PCM back into `whisper-large-v3-turbo` on EcoHash; the transcription came back word for word.

## Notes

- Return exactly the `sampleRate` Vapi asks for (8000, 16000, 22050, or 24000). Kokoro is 24 kHz native; the adapter resamples.
- Live call transcription stays on Vapi's built-in transcribers: the custom transcriber slot expects a streaming WebSocket, and EcoHash's transcription endpoint is batch. Use `whisper-large-v3-turbo` for post-call transcription.
- Cost comparison against ElevenLabs, the custom-LLM bonus, and the FAQ are in the tutorial: https://ecohash.com/blog/vapi-custom-tts-kokoro
