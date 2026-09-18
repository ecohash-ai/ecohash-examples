#!/usr/bin/env python3
"""Check that this repo is ready to run: key, connectivity, and model availability.

Run this once after setting ECOHASH_API_KEY and before the first example:

    python check_setup.py

It scans every example in this repo for the model ids they use, compares them
against the live catalog, and makes one tiny chat request to confirm the key
works. Nothing here prints your key. Total cost is under $0.0001.
"""

import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

BASE_URL = "https://api.ecohash.com/v1"
CATALOG_URL = "https://api.ecohash.com/platform/models"
CONSOLE = ("https://console.ecohash.com?utm_source=github&utm_medium=referral"
           "&utm_campaign=devrel&utm_content=examples-check-setup")
PROBE_MODEL = "llama-3.1-8b-instruct"
HERE = Path(__file__).resolve().parent

# Matches model="x", "model": "x", and MODEL = "x" in the example sources.
MODEL_PATTERNS = [
    re.compile(r'\bmodel\s*=\s*"([^"]+)"'),
    re.compile(r'"model"\s*:\s*"([^"]+)"'),
    re.compile(r'\b[A-Z_]*MODEL\s*=\s*"([^"]+)"'),
]

ok = True


def fail(msg, fix):
    global ok
    ok = False
    print(f"  FAIL  {msg}")
    for line in fix.splitlines():
        print(f"        {line}")


def get(url, key=None, timeout=30):
    headers = {"Authorization": f"Bearer {key}"} if key else {}
    req = urllib.request.Request(url, headers=headers)
    return json.load(urllib.request.urlopen(req, timeout=timeout))


def models_used():
    """Every model id referenced by the examples, with the files that use it."""
    found = {}
    for path in sorted(HERE.rglob("*.py")):
        if path.name == "check_setup.py" or ".venv" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in MODEL_PATTERNS:
            for name in pattern.findall(text):
                found.setdefault(name, set()).add(str(path.relative_to(HERE)))
    return found


print("EcoHash examples: setup check\n")

# 1. Key present and shaped like a key.
key = os.environ.get("ECOHASH_API_KEY")
if not key:
    fail("ECOHASH_API_KEY is not set.",
         f"Create a key at {CONSOLE}\nThen: export ECOHASH_API_KEY=eco_...")
    sys.exit(1)
if not key.startswith("eco_"):
    fail("ECOHASH_API_KEY does not start with 'eco_'.",
         "EcoHash keys begin with eco_. Check that you copied the whole value\n"
         "and did not paste a key from another provider.")
    sys.exit(1)
print(f"  OK    key is set (eco_...{key[-4:]})")

# 2. Key works, and the API is reachable.
body = json.dumps({"model": PROBE_MODEL,
                   "messages": [{"role": "user", "content": "ping"}],
                   "max_tokens": 1}).encode()
req = urllib.request.Request(f"{BASE_URL}/chat/completions", data=body,
                             headers={"Authorization": f"Bearer {key}",
                                      "Content-Type": "application/json"})
try:
    urllib.request.urlopen(req, timeout=60)
    print(f"  OK    API reachable, key accepted ({PROBE_MODEL})")
except urllib.error.HTTPError as e:
    detail = e.read().decode(errors="replace")[:200]
    if e.code == 401:
        fail(f"401 unauthorized: {detail}",
             f"The key was rejected. Check it is active and not revoked at {CONSOLE}\n"
             "A key pasted with a trailing space or newline also fails this way.")
    elif e.code == 429:
        fail(f"429 rate limited: {detail}",
             "You are over your rate or spend limit. Wait and retry, or raise the\n"
             f"limit on your account at {CONSOLE}\n"
             "In your own code, retry with exponential backoff; the OpenAI SDK\n"
             "does this for you when you pass max_retries.")
    elif e.code == 404:
        fail(f"404 model not found: {detail}",
             f"{PROBE_MODEL} is no longer served. Pick another id from\n"
             f"{CATALOG_URL} and open an issue so we can fix the examples.")
    else:
        fail(f"HTTP {e.code}: {detail}", "Unexpected response. Please open an issue with this output.")
    sys.exit(1)
except urllib.error.URLError as e:
    fail(f"cannot reach {BASE_URL}: {e.reason}",
         "Check your network or proxy. The examples need outbound HTTPS to\n"
         "api.ecohash.com.")
    sys.exit(1)

# 3. Every model the examples reference is live.
try:
    catalog = {m["model_id"]: m for m in get(CATALOG_URL)}
except Exception as e:  # noqa: BLE001 - the catalog is public and unauthenticated
    fail(f"could not read the model catalog: {e}",
         f"Skipping the drift check. You can read it yourself at {CATALOG_URL}")
    sys.exit(1)

used = models_used()
missing = {name: files for name, files in used.items() if name not in catalog}
inactive = {name: files for name, files in used.items()
            if name in catalog and catalog[name].get("status") != "active"}

print(f"  OK    catalog has {len(catalog)} models; examples reference {len(used)}")
for name, files in sorted(missing.items()):
    fail(f"{name} is not in the catalog (used in {', '.join(sorted(files))})",
         "The examples are out of date. Please open an issue; meanwhile pick a\n"
         f"replacement from {CATALOG_URL}")
for name, files in sorted(inactive.items()):
    fail(f"{name} is {catalog[name].get('status')} (used in {', '.join(sorted(files))})",
         "This model is listed but not serving. Please open an issue.")

print()
if ok:
    print("All checks passed. Start with: cd quickstart/chatbot && python chat.py")
    sys.exit(0)
print("Some checks failed. See the fixes above, or the Troubleshooting section in README.md.")
sys.exit(1)
