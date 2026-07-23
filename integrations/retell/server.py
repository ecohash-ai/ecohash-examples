"""Retell custom-LLM bridge for EcoHash.

Retell connects to this WebSocket server during a call and streams transcript
events; the bridge answers by streaming chat completions from EcoHash's
OpenAI-compatible API. Point the agent's "Custom LLM" URL at
wss://your-host/llm-websocket and the agent's brain runs on an open model.

Run:
    pip install fastapi uvicorn openai
    export ECOHASH_API_KEY=eco_...   # create one at console.ecohash.com
    uvicorn server:app --host 0.0.0.0 --port 8000
"""

import asyncio
import os

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from openai import AsyncOpenAI

ECOHASH_MODEL = "llama-3.1-8b-instruct"
BEGIN_SENTENCE = "Hi, thanks for calling. How can I help you today?"
SYSTEM_PROMPT = (
    "You are a friendly voice assistant on a live phone call. "
    "Reply in short, natural spoken sentences, one point at a time. "
    "The transcript comes from speech recognition, so expect small errors "
    "and guess the intent instead of asking for spelling."
)

client = AsyncOpenAI(
    base_url="https://api.ecohash.com/v1",
    api_key=os.environ["ECOHASH_API_KEY"],
)

app = FastAPI()


def to_messages(transcript: list[dict]) -> list[dict]:
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for u in transcript:
        role = "assistant" if u.get("role") == "agent" else "user"
        messages.append({"role": role, "content": u.get("content", "")})
    return messages


@app.websocket("/llm-websocket/{call_id}")
async def llm_websocket(ws: WebSocket, call_id: str):
    await ws.accept()

    # Tell Retell how this server behaves, then speak first.
    await ws.send_json({"response_type": "config",
                        "config": {"auto_reconnect": True, "call_details": False}})
    await ws.send_json({"response_type": "response", "response_id": 0,
                        "content": BEGIN_SENTENCE, "content_complete": True,
                        "end_call": False})

    latest_id = 0  # newer response_id supersedes any reply still streaming

    async def reply(request: dict):
        nonlocal latest_id
        response_id = request["response_id"]
        stream = await client.chat.completions.create(
            model=ECOHASH_MODEL,
            messages=to_messages(request.get("transcript", [])),
            stream=True,
        )
        async for chunk in stream:
            if response_id < latest_id:  # user spoke again; drop stale reply
                await stream.close()
                return
            if not chunk.choices:
                continue
            delta = chunk.choices[0].delta.content or ""
            if delta:
                await ws.send_json({"response_type": "response",
                                    "response_id": response_id, "content": delta,
                                    "content_complete": False, "end_call": False})
        await ws.send_json({"response_type": "response", "response_id": response_id,
                            "content": "", "content_complete": True, "end_call": False})

    try:
        async for event in ws.iter_json():
            kind = event.get("interaction_type")
            if kind == "ping_pong":
                await ws.send_json({"response_type": "ping_pong",
                                    "timestamp": event.get("timestamp")})
            elif kind in ("response_required", "reminder_required"):
                latest_id = event["response_id"]
                asyncio.create_task(reply(event))
            # call_details / update_only need no reply
    except WebSocketDisconnect:
        pass
