"""Synthesize speech with EcoHash (OpenAI-compatible)."""

import os
import sys

from openai import OpenAI

api_key = os.environ.get("ECOHASH_API_KEY")
if not api_key:
    sys.exit("ECOHASH_API_KEY is not set. Create a key at https://console.ecohash.com"
             "?utm_source=github&utm_medium=referral&utm_campaign=devrel"
             "&utm_content=examples-text-to-speech-missing-key, "

             "then: export ECOHASH_API_KEY=eco_...")

client = OpenAI(
    base_url="https://api.ecohash.com/v1",
    api_key=api_key,
)

with client.audio.speech.with_streaming_response.create(
    model="kokoro-82m",
    voice="af_heart",           # other voices available, see docs
    input="Hello from EcoHash.",
    response_format="wav",      # also: "mp3", "opus"
    speed=1.0,                  # 0.5–2.0
) as response:
    response.stream_to_file("speech.wav")

print("wrote speech.wav")
