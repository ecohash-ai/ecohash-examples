"""Synthesize speech with EcoHash (OpenAI-compatible)."""

import os

from openai import OpenAI

client = OpenAI(
    base_url="https://api.ecohash.com/v1",
    api_key=os.environ["ECOHASH_API_KEY"],
)

with client.audio.speech.with_streaming_response.create(
    model="kokoro-82m",
    voice="af_heart",           # other voices available — see docs
    input="Hello from EcoHash.",
    response_format="wav",      # also: "mp3", "opus"
    speed=1.0,                  # 0.5–2.0
) as response:
    response.stream_to_file("speech.wav")

print("wrote speech.wav")
