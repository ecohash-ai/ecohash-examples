<p align="center">
  <a href="https://ecohash.com?utm_source=github&utm_medium=referral&utm_campaign=devrel&utm_content=examples-readme-logo"><img src="assets/ecohash-logo.png" alt="EcoHash" width="280"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-blue" alt="MIT">
  <a href="https://docs.ecohash.com?utm_source=github&utm_medium=referral&utm_campaign=devrel&utm_content=examples-readme-docs"><img src="https://img.shields.io/badge/documentation-6D28D9" alt="Documentation"></a>
  <a href="https://x.com/ecohashdev"><img src="https://img.shields.io/badge/X-@ecohashdev-000000?logo=x&logoColor=white" alt="X"></a>
  <a href="https://huggingface.co/ecohash-ai"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-ecohash--ai-FFD21E" alt="Hugging Face"></a>
</p>

# EcoHash Examples

Runnable examples for [EcoHash](https://ecohash.com?utm_source=github&utm_medium=referral&utm_campaign=devrel&utm_content=examples-readme-intro), an OpenAI-compatible inference API for open models: chat, speech, embeddings, reranking and images, all on one key.

Each example is one short file, meant to be read as much as run.

## Get to a first result

Five steps, about three minutes. The whole path costs well under a cent.

**1. Clone and enter the repo**

```bash
git clone https://github.com/ecohash-ai/ecohash-examples.git
cd ecohash-examples
```

**2. Create a virtual environment**

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
```

**3. Install the dependencies**

```bash
pip install -r requirements.txt
```

**4. Set your API key**

Create one at [console.ecohash.com](https://console.ecohash.com?utm_source=github&utm_medium=referral&utm_campaign=devrel&utm_content=examples-readme-console), open **API Keys**, and copy the `eco_` value.

```bash
export ECOHASH_API_KEY=eco_...   # Windows: set ECOHASH_API_KEY=eco_...
```

Keep the key in the environment. Do not paste it into a URL, a commit, or an issue.

**5. Check the setup, then run your first example**

```bash
python check_setup.py
```

```
EcoHash examples: setup check

  OK    key is set (eco_...9B2E)
  OK    API reachable, key accepted (llama-3.1-8b-instruct)
  OK    catalog has 39 models; examples reference 7

All checks passed. Start with: cd quickstart/chatbot && python chat.py
```

`check_setup.py` verifies your key, reaches the API, and confirms that every model these examples reference is still being served. It never prints your key. When something is wrong it names the fix.

Now run the streaming chat example, which needs no input:

```bash
cd quickstart/streaming-chat
python stream.py
```

```
Here is a haiku about open source:

Code shared freely flows
Collaboration's sweet gift
Freedom's open door
```

The wording differs each run. If a haiku appeared word by word, everything works.

### Tested versions

Last run end to end on 2026-09-18:

| | Version |
|---|---|
| Python | 3.12.13, and 3.9.6 as the supported floor |
| openai | 3.15.0 on 3.12, 2.48.0 on 3.9 |
| requests | 2.34.2 on 3.12, 2.32.5 on 3.9 |
| Platform | macOS 15 (darwin 24.5.0) |

Both major versions of the OpenAI SDK work without code changes. All nine examples pass on both; [docs/verification.md](docs/verification.md) has the commands and the output of each one.

## The examples

Each folder has its own README with the pip line, the run command, and the output to expect.

### Text

| Example | What it shows |
|---|---|
| [chatbot](quickstart/chatbot) | multi-turn chat that remembers earlier turns |
| [streaming-chat](quickstart/streaming-chat) | stream tokens as they are generated |
| [function-calling](quickstart/function-calling) | the full tool-use loop, request through final answer |

### Voice and speech

| Example | What it shows |
|---|---|
| [voice-agent](voice-agent) | speech-to-text, LLM and text-to-speech on one key |
| [speech-to-text](quickstart/speech-to-text) | transcribe an audio file |
| [text-to-speech](quickstart/text-to-speech) | synthesize speech to a `.wav` |

### Retrieval

| Example | What it shows |
|---|---|
| [embeddings](quickstart/embeddings) | rank documents by meaning, no vector database |
| [reranker](quickstart/reranker) | reorder candidates as a second RAG stage |

### Images

| Example | What it shows |
|---|---|
| [image-generation](quickstart/image-generation) | text prompt to PNG |

### Platform integrations

| Integration | What it does |
|---|---|
| [vapi](integrations/vapi) | Kokoro TTS as the voice of a Vapi agent |
| [retell](integrations/retell) | an open model as the brain of a Retell AI agent |

More in [integrations](integrations). The Dify plugin lives in its own repo, [ecohash-dify-plugin](https://github.com/ecohash-ai/ecohash-dify-plugin).

## Point your own code at EcoHash

Any OpenAI client works once you change two fields:

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.ecohash.com/v1", api_key="eco_...")
```

Browse the models and prices at [ecohash.com/models](https://ecohash.com/models?utm_source=github&utm_medium=referral&utm_campaign=devrel&utm_content=examples-readme-models). The live catalog is public JSON at `https://api.ecohash.com/platform/models`, which is what `check_setup.py` reads.

## Troubleshooting

`python check_setup.py` detects all of these and prints the fix. The table is here for when you hit one inside your own code.

| What you see | What it means | What to do |
|---|---|---|
| `ECOHASH_API_KEY is not set` | the environment variable is missing | `export ECOHASH_API_KEY=eco_...` in the same shell that runs the example. A new terminal tab does not inherit it. |
| `AuthenticationError: Error code: 401 - {'error': 'unauthorized'}` | the key was rejected | Check that the key is active in the console. A trailing space or newline from copy and paste fails the same way. |
| `RateLimitError: Error code: 429` | over your rate or spend limit | Wait and retry. In your own code pass `OpenAI(..., max_retries=5)` so the SDK backs off for you. |
| `NotFoundError: Error code: 404 - {'error': 'model not found: ...'}` | that model id is no longer served | Pick a current id from [ecohash.com/models](https://ecohash.com/models?utm_source=github&utm_medium=referral&utm_campaign=devrel&utm_content=examples-readme-models-404). If an example in this repo caused it, please open an issue, because that is a bug on our side. |
| `ModuleNotFoundError: No module named 'openai'` | the virtual environment is not active | `source .venv/bin/activate`, then `pip install -r requirements.txt`. |

## More

- [How EcoHash compares to other providers](docs/comparison.md)
- [Verification log: what was run, when, and with which versions](docs/verification.md)
- [Live smoke test: the procedure and its cost limits](docs/smoke-test.md)
- Documentation: [docs.ecohash.com](https://docs.ecohash.com?utm_source=github&utm_medium=referral&utm_campaign=devrel&utm_content=examples-readme-docs-footer)
- Benchmarks: [ecohash-benchmarks](https://github.com/ecohash-ai/ecohash-benchmarks)
- Questions or bugs: open an issue in this repo.

## License

MIT, see [LICENSE](LICENSE).
