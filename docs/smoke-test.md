# Live smoke test

These examples call a paid API, so they cannot be checked by a build that never
touches the network. This is the procedure we run instead: bounded in cost, bounded in
scope, and safe to run without leaking a key.

## The budget

One full pass over all nine examples costs **$0.0113** at the 2026-09-18 catalog
prices. Image generation is $0.01 of that, so 88% of a run is one call.

| Example | Billing | Cost per run |
|---|---|---|
| image-generation | 1,000 tokens per image at $10 / 1M | $0.0100 |
| voice-agent | 3.8s in at $0.10 / 1M, ~3s out at $1 / 1M, plus chat | $0.0007 |
| speech-to-text | 1,000 tokens per audio second at $0.10 / 1M | $0.0004 |
| text-to-speech | 100 tokens per audio second at $1 / 1M | $0.0001 |
| function-calling | two chat calls at $0.10 in / $0.30 out per 1M | $0.00005 |
| chatbot | two turns at $0.10 / 1M | $0.00001 |
| streaming-chat | one short completion | $0.000005 |
| reranker, embeddings, check_setup.py | a few dozen tokens each | under $0.000005 |

The per-unit numbers come from the public catalog: each entry carries
`billing_meter`, `image_tokens_per_image`, `audio_input_tokens_per_sec` and
`audio_output_tokens_per_sec` alongside the per-million price. Recompute rather than
trusting this table if you need a current figure.

Limits we hold ourselves to:

- Per run, $0.05. That is four times the measured cost. A run that approaches it means
  something is looping or a price changed, so stop and look rather than pay.
- Per month, $1.00. Enough for a weekly pass plus reruns after a fix.
- Set the cap on the key itself in the console, so the platform enforces it rather than
  the person running the test.

## When to run it

- Weekly.
- Before changing any model id, any pinned version, or any expected output in a README.
- After a catalog change lands, because that is what retires model ids underneath us.

`python check_setup.py` alone costs a fraction of a cent and catches the failure that
actually recurs, which is a model id going away. Run it freely. The full pass is for
the weekly check and for release gates.

## How to run it safely

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

read -rs ECOHASH_API_KEY && export ECOHASH_API_KEY    # prompts without echoing
python check_setup.py
```

Then run each example from its own directory, as its README says.

Rules for the key:

- It lives in the environment for the length of the shell session and nowhere else.
  Not in a file in the repo, not in a URL, not in a shell history line.
- `read -rs` keeps it out of your shell history and off the screen. Typing
  `export ECOHASH_API_KEY=eco_...` directly puts it in `~/.zsh_history`.
- Use a smoke-test key with its own spend cap, not a production key. Rotate it if it
  ever lands in a log.
- `check_setup.py` prints only the last four characters of the key. Keep it that way.
- Before pasting output anywhere, run it through
  `sed -E 's/eco_[A-Za-z0-9_-]+/eco_REDACTED/g'`.

## What a pass looks like

Each README states the output to expect. Model output is not deterministic, so match
on shape rather than on exact words: the haiku is three lines, the weather answer names
Dallas and 21°C, the embedding ranking puts the console document first, the transcript
matches the spoken sentence, and the files land on disk at roughly the sizes given.

The last full pass, with real output for every example, is in
[verification.md](verification.md).

## Why there is no CI job

We decided not to add a GitHub Actions workflow for this. Doing it properly would mean
putting a live, funded API key in repository secrets on a public repo, and the thing
most worth catching, a model disappearing from the catalog, is caught by
`check_setup.py` in one command. The cost is that nothing runs automatically on a pull
request. We run this procedure by hand on the schedule above.
