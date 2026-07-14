"""Vapi custom-voice adapter for EcoHash TTS (Kokoro).

Vapi POSTs a voice-request and expects raw PCM back (16-bit mono little-endian,
at the exact sample rate it asks for). This server forwards the text to EcoHash's
OpenAI-compatible /v1/audio/speech, resamples when needed, and returns the PCM.

Run:
    pip install fastapi uvicorn httpx numpy
    export ECOHASH_API_KEY=eco_...          # create one at console.ecohash.com
    export VAPI_SECRET=your-webhook-secret  # optional; must match the assistant config
    uvicorn server:app --host 0.0.0.0 --port 8000
"""

import os

import httpx
import numpy as np
from fastapi import FastAPI, HTTPException, Request, Response

ECOHASH_BASE = "https://api.ecohash.com/v1"
ECOHASH_KEY = os.environ["ECOHASH_API_KEY"]
VAPI_SECRET = os.environ.get("VAPI_SECRET")  # if set, requests must carry it

TTS_MODEL = "kokoro-82m"
TTS_VOICE = "af_heart"
NATIVE_RATE = 24000  # kokoro-82m outputs 24 kHz mono 16-bit PCM

app = FastAPI()


def resample(pcm: bytes, src_rate: int, dst_rate: int) -> bytes:
    if src_rate == dst_rate:
        return pcm
    samples = np.frombuffer(pcm, dtype=np.int16)
    n_out = int(len(samples) * dst_rate / src_rate)
    x_out = np.linspace(0, len(samples) - 1, n_out)
    out = np.interp(x_out, np.arange(len(samples)), samples.astype(np.float32))
    return out.astype(np.int16).tobytes()


@app.post("/synthesize")
async def synthesize(request: Request) -> Response:
    if VAPI_SECRET and request.headers.get("x-vapi-secret") != VAPI_SECRET:
        raise HTTPException(status_code=401, detail="bad or missing x-vapi-secret")

    body = await request.json()
    msg = body.get("message", {})
    if msg.get("type") != "voice-request":
        raise HTTPException(status_code=400, detail="expected message.type=voice-request")

    text = msg.get("text", "")
    sample_rate = int(msg.get("sampleRate", NATIVE_RATE))
    if not text:
        raise HTTPException(status_code=400, detail="empty text")

    async with httpx.AsyncClient(timeout=30) as client:
        r = await client.post(
            f"{ECOHASH_BASE}/audio/speech",
            headers={"Authorization": f"Bearer {ECOHASH_KEY}"},
            json={
                "model": TTS_MODEL,
                "voice": TTS_VOICE,
                "input": text,
                "response_format": "pcm",
            },
        )
    if r.status_code != 200:
        raise HTTPException(status_code=502, detail=f"EcoHash TTS error {r.status_code}")

    pcm = resample(r.content, NATIVE_RATE, sample_rate)
    return Response(content=pcm, media_type="application/octet-stream")
