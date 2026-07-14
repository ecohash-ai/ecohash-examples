"""Transcribe an audio file with EcoHash (OpenAI-compatible)."""

import os
import sys

from openai import OpenAI

client = OpenAI(
    base_url="https://api.ecohash.com/v1",
    api_key=os.environ["ECOHASH_API_KEY"],
)

audio_path = sys.argv[1] if len(sys.argv) > 1 else "audio.wav"

with open(audio_path, "rb") as audio_file:
    result = client.audio.transcriptions.create(
        model="whisper-large-v3",
        file=audio_file,
        # response_format: "json" (default) | "text" | "srt" | "vtt" | "verbose_json" (segment timestamps)
        # language="en",           # skip language auto-detect for a known language
        # prompt="Domain terms.",  # bias transcription toward specific vocabulary
    )

print(result.text)
