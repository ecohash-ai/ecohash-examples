"""Voice agent on EcoHash: speech-to-text -> LLM -> text-to-speech, one API key.

Usage:
  python agent.py input.wav      transcribe a .wav, reply, write reply.wav
  python agent.py --mic          record from the mic each turn (pip install sounddevice numpy)

Conversation history is kept within a run, so the assistant remembers earlier turns.
"""

import io
import os
import sys
import wave

from openai import OpenAI

client = OpenAI(
    base_url="https://api.ecohash.com/v1",
    api_key=os.environ["ECOHASH_API_KEY"],
)

STT_MODEL = "whisper-large-v3"
LLM_MODEL = "llama-3.1-8b-instruct"
TTS_MODEL = "kokoro-82m"
VOICE = "af_heart"

history = [{"role": "system", "content": "You are a concise, friendly voice assistant. Keep replies short."}]


def transcribe(wav_bytes):
    return client.audio.transcriptions.create(
        model=STT_MODEL, file=("input.wav", wav_bytes, "audio/wav")
    ).text


def respond(text):
    history.append({"role": "user", "content": text})
    answer = client.chat.completions.create(model=LLM_MODEL, messages=history).choices[0].message.content
    history.append({"role": "assistant", "content": answer})
    return answer


def synthesize(text, path):
    with client.audio.speech.with_streaming_response.create(
        model=TTS_MODEL, voice=VOICE, input=text, response_format="wav"
    ) as response:
        response.stream_to_file(path)


def run_turn(wav_bytes, out_path):
    user = transcribe(wav_bytes)
    print("You:", user)
    answer = respond(user)
    print("Assistant:", answer)
    synthesize(answer, out_path)
    print("Wrote", out_path)


def record(seconds=5, sr=16000):
    import sounddevice as sd
    print(f"Recording {seconds}s — speak now…")
    audio = sd.rec(int(seconds * sr), samplerate=sr, channels=1, dtype="int16")
    sd.wait()
    buf = io.BytesIO()
    with wave.open(buf, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes(audio.tobytes())
    return buf.getvalue()


if len(sys.argv) > 1 and sys.argv[1] == "--mic":
    print("Voice agent (mic mode). Press Ctrl-C to quit.")
    turn = 0
    while True:
        turn += 1
        run_turn(record(), f"reply{turn}.wav")
else:
    path = sys.argv[1] if len(sys.argv) > 1 else "input.wav"
    with open(path, "rb") as f:
        run_turn(f.read(), "reply.wav")
