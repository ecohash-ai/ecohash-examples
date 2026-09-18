# Verification log

What was run, when, and what came back. The procedure and its cost limits are in
[smoke-test.md](smoke-test.md).

## 2026-09-18

**Setup.** Fresh copy of the repo, new virtualenv, `pip install -r requirements.txt`,
key supplied through `ECOHASH_API_KEY`. Every example run from its own directory, as
its README instructs.

| | |
|---|---|
| Python | 3.12.13 (main run), 3.9.6 (floor run) |
| openai | 3.15.0 on 3.12, 2.48.0 on 3.9 |
| requests | 2.34.2 on 3.12, 2.32.5 on 3.9 |
| Platform | macOS 15, darwin 24.5.0, arm64 |
| Catalog | 39 models, read from `https://api.ecohash.com/platform/models` |
| Cost | $0.0113 for the full pass |

**Results.** All nine pass on both Python versions.

| Example | Model | Result |
|---|---|---|
| check_setup.py | llama-3.1-8b-instruct | 3 checks pass, 7 referenced models all live |
| streaming-chat | llama-3.1-8b-instruct | three-line haiku, streamed |
| chatbot | llama-3.1-8b-instruct | two turns, second answer recalls the name from the first |
| function-calling | qwen3-coder-30b-a3b-instruct | tool call issued and answered: `The weather in Dallas is sunny with a temperature of 21°C.` |
| embeddings | jina-embeddings-v3 | console document ranks first at 0.691, correct order |
| reranker | bge-reranker-v2-m3 | `0 0.399`, `2 0.016`; the cat document correctly dropped by `top_n: 2` |
| speech-to-text | whisper-large-v3-turbo | transcript matches the spoken sentence exactly |
| text-to-speech | kokoro-82m | `speech.wav`, 73,486 bytes |
| image-generation | z-image-turbo | `image.png`, 1024x1024 RGB PNG, 1,379,293 bytes, a watercolor fox in a misty forest as prompted |
| voice-agent | whisper-large-v3-turbo, llama-3.1-8b-instruct, kokoro-82m | transcript, reply, `reply.wav` at 369,752 bytes |

The audio input for the speech examples was generated on the spot with the two `say`
and `afconvert` commands printed in
[quickstart/speech-to-text/README.md](../quickstart/speech-to-text/README.md), so the
path a reader follows is the path that was tested.

**Error paths.** Checked by hand, all four give an actionable message rather than a
traceback:

| Condition | Behaviour |
|---|---|
| `ECOHASH_API_KEY` unset | one line naming the variable, the console URL, and the `export` to run |
| key from another provider (no `eco_` prefix) | caught before any network call, with the reason |
| revoked or mistyped key | `401 unauthorized`, plus the note that a trailing newline from copy and paste fails identically |
| model id no longer in the catalog | `check_setup.py` names the model and the file that uses it |

The last one was verified by putting a retired id back into a scratch copy of the
repo. `check_setup.py` reported
`whisper-large-v3 is not in the catalog (used in quickstart/speech-to-text/transcribe.py)`
and exited non-zero.

## What this run fixed

Five model ids in the repo were no longer being served, and two of them were in code
rather than prose, so those examples failed outright:

| Stale id | Was in | Replaced with |
|---|---|---|
| `qwen2.5-7b-instruct` | `quickstart/function-calling/tools.py`, two READMEs | `qwen3-coder-30b-a3b-instruct` |
| `whisper-large-v3` | `quickstart/speech-to-text/transcribe.py`, `voice-agent/agent.py`, `voice-agent/diagram.py`, two READMEs | `whisper-large-v3-turbo` |
| `Qwen3-235B-A22B` | chatbot README | dropped |
| `qwen3-embedding-8b`, `qwen3-embedding-4b` | embeddings README | `jina-embeddings-v4`, `qwen3-embedding-0.6b` |

`quickstart/function-calling/tools.py` and `quickstart/speech-to-text/transcribe.py`
both ended in a `NotFoundError` traceback before this. The replacements were chosen
from the catalog rather than guessed: the tool-calling model is the cheapest entry
carrying `agent_capable: true`, and both were run before being committed.

`check_setup.py` exists so this class of breakage is caught in one command instead of
by a reader.

## Known limitations

- **No CI.** Nothing runs automatically on a pull request. The reasoning and the
  manual schedule that replaces it are in [smoke-test.md](smoke-test.md).
- **Not deterministic.** Model output varies between runs, so the outputs quoted in
  the READMEs are examples of shape, not strings to assert on.
- **macOS only for the audio helper.** The `say` and `afconvert` commands that make a
  test `.wav` are macOS tools. On Linux, supply your own audio file.
- **`--mic` untested here.** The voice agent's microphone mode needs `sounddevice` and
  an input device; only the file mode was run.
- **Integrations not re-run.** The Vapi and Retell bridges were verified when they
  were written and are not part of this pass; they need an account on those platforms
  and a publicly reachable port. Their model ids were checked against the catalog.
